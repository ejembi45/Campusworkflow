import json
import re
from pathlib import Path

from campusflow.service import TicketService
from campusflow.storage import TicketStorage
from campusflow.reports import generate_report


DATA_FILE = Path(__file__).parent / "data" / "tickets.json"


def read_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def read_ticket_id(prompt="Ticket ID: "):
    ticket_id = input(prompt).strip().upper()
    if not re.fullmatch(r"T\d{3,}", ticket_id):
        raise ValueError("Ticket ID must use the format T001")
    return ticket_id


def show_ticket(ticket):
    print("\n--- Ticket Details ---")
    print(f"ID: {ticket['id']}")
    print(f"Title: {ticket['title']}")
    print(f"Category: {ticket['category']}")
    print(f"Urgency: {ticket['urgency']}")
    print(f"Affected users: {ticket['affected_users']}")
    print(f"Priority: {ticket['priority']}")
    print(f"Status: {ticket['status']}")
    print(f"Assigned to: {ticket['assigned_to'] or 'Unassigned'}")


def create_new_ticket(service):
    title = input("Problem title: ").strip()
    category = input("Category: ").strip()
    urgency = input("Urgency (high/medium/low): ").strip().lower()
    affected_users = read_integer("Number of affected users: ")

    tickets = service.get_all()
    ticket_id = "T{:03d}".format(max((int(ticket["id"][1:]) for ticket in tickets), default=0) + 1)

    ticket = service.create(
        ticket_id, title, category, urgency, affected_users
    )
    print(f"\nTicket {ticket['id']} created successfully.")
    show_ticket(ticket)


def list_tickets(service):
    tickets = service.get_all()

    if not tickets:
        print("\nNo tickets have been created yet.")
        return

    for ticket in tickets:
        print(
            f"{ticket['id']} | {ticket['priority']} | "
            f"{ticket['status']} | {ticket['title']} | "
            f"Assigned to: {ticket['assigned_to'] or 'Nobody'}"
        )


def find_ticket(service):
    ticket_id = read_ticket_id()
    show_ticket(service.get(ticket_id))


def assign_ticket(service):
    ticket_id = read_ticket_id()
    staff_name = input("Staff member's name: ").strip()
    show_ticket(service.assign(ticket_id, staff_name))


def change_status(service, action):
    ticket_id = read_ticket_id()

    actions = {
        "start": service.start,
        "resolve": service.resolve,
        "reopen": service.reopen,
        "close": service.close,
    }

    show_ticket(actions[action](ticket_id))


def list_unresolved(service):
    tickets = [
        ticket for ticket in service.get_all()
        if ticket["status"] not in ("resolved", "closed")
    ]

    tickets.sort(
        key=lambda ticket: (
            {"critical": 0, "high": 1, "medium": 2, "low": 3}[
                ticket["priority"]
            ],
            int(ticket["id"][1:]),
        )
    )

    if not tickets:
        print("\nThere are no unresolved tickets.")
        return

    print("\n--- Unresolved Tickets (highest priority first) ---")
    for ticket in tickets:
        print(
            f"{ticket['id']} | {ticket['priority']} | "
            f"{ticket['status']} | {ticket['title']}"
        )


def show_report(service):
    report = generate_report(service.get_all())

    print("\n--- CampusFlow Report ---")
    print(f"Total tickets: {report['total']}")

    print("\nBy status:")
    for status, count in report["by_status"].items():
        print(f"  {status}: {count}")

    print("\nBy priority:")
    for priority, count in report["by_priority"].items():
        print(f"  {priority}: {count}")

    print(f"\nTotal affected users: {report['total_affected_users']}")
    print(f"Affected users on closed tickets: {report['closed_affected_users']}")


def main():
    storage = TicketStorage(DATA_FILE)
    service = TicketService(storage)

    actions = {
        "1": ("Create ticket", lambda: create_new_ticket(service)),
        "2": ("List all tickets", lambda: list_tickets(service)),
        "3": ("View ticket details", lambda: find_ticket(service)),
        "4": ("Assign ticket", lambda: assign_ticket(service)),
        "5": ("Start ticket work", lambda: change_status(service, "start")),
        "6": ("Resolve ticket", lambda: change_status(service, "resolve")),
        "7": ("Reopen ticket", lambda: change_status(service, "reopen")),
        "8": ("Close ticket", lambda: change_status(service, "close")),
        "9": ("View unresolved queue", lambda: list_unresolved(service)),
        "10": ("Generate report", lambda: show_report(service)),
    }

    while True:
        print("\n========== CampusFlow ==========")
        for number, (label, _) in actions.items():
            print(f"{number}. {label}")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Thank you for using CampusFlow.")
            break

        if choice not in actions:
            print("Invalid option. Please choose from the menu.")
            continue

        try:
            actions[choice][1]()
        except (ValueError, KeyError) as error:
            print(f"Operation failed: {error}")
        except OSError as error:
            print(f"File operation failed: {error}")


if __name__ == "__main__":
    main()
