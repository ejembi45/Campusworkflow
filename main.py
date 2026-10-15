import re
from pathlib import Path

from campusflow.service import TicketService
from campusflow.storage import TicketStorage
from campusflow.reports import generate_report
from campusflow.quiz import QUESTIONS, score_answers
from campusflow.search import (
    VALID_CATEGORIES,
    VALID_PRIORITIES,
    VALID_STATUSES,
    sort_by_priority,
)


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
    affected_users = read_integer("Number of affected users: ", minimum=1)

    tickets = service.get_all()
    ticket_id = "T{:03d}".format(
        max((int(ticket["id"][1:]) for ticket in tickets), default=0) + 1
    )

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


def prompt_filter(label, valid_values):
    """Prompt for an optional filter value, re-prompting until it is valid.

    Returns the canonical value, or ``None`` when the user presses Enter.
    Invalid options re-prompt instead of ending the search.
    """
    options = "/".join(valid_values)
    prompt = f"{label} ({options}, or Enter to skip): "

    while True:
        raw = input(prompt).strip()

        if not raw:
            return None

        normalized = raw.casefold()

        for value in valid_values:
            if value.casefold() == normalized:
                return value

        print(
            f"Invalid {label.lower()}. Choose one of {options}, "
            "or press Enter to skip."
        )


def collect_search(service):
    """Read a title search plus optional filters and run the search.

    Empty filters are not applied. All supplied filters must match.
    """
    title = input("Enter title or part of title to search: ").strip()

    while not title:
        print("Search title cannot be empty.")
        title = input("Enter title or part of title to search: ").strip()

    category = prompt_filter("Category", VALID_CATEGORIES)
    status = prompt_filter("Status", VALID_STATUSES)
    priority = prompt_filter("Priority", VALID_PRIORITIES)

    tickets = service.filter(
        title=title,
        category=category,
        status=status,
        priority=priority,
    )

    return title, tickets


def display_search_results(tickets, title, ordered=False):
    if not tickets:
        print(
            f"No tickets found matching '{title}' "
            "with the supplied filters."
        )
        return

    heading = "priority order" if ordered else "best match order"

    print(f"\n--- Search Results, {heading} ({len(tickets)} found) ---")
    for ticket in tickets:
        print(
            f"{ticket['id']} | {ticket['title']} | "
            f"{ticket['category']} | {ticket['priority']} | "
            f"{ticket['status']} | "
            f"Assigned to: {ticket['assigned_to'] or 'Unassigned'}"
        )


def search_tickets_by_title(service):
    title, tickets = collect_search(service)
    display_search_results(tickets, title)


def search_tickets_sorted(service):
    """Optional view: search results sorted by priority then ticket ID."""
    title, tickets = collect_search(service)
    display_search_results(sort_by_priority(tickets), title, ordered=True)


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
        if ticket["status"] == "open"
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
        print("\nThere are no open tickets.")
        return

    print("\n--- Open Work Queue (highest priority first) ---")
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

    print("\nBy category:")
    for category, count in report["by_category"].items():
        print(f"  {category}: {count}")

    print(f"\nUnresolved tickets (open + in_progress): "
          f"{report['unresolved_count']}")
    print(f"Resolved tickets: {report['resolved_count']}")
    print(f"Resolution percentage: {report['resolution_percentage']:.1f}%")

    print(f"\nTotal affected users: {report['total_affected_users']}")
    print(
        f"Affected users on closed tickets: "
        f"{report['closed_affected_users']}"
    )


def add_ticket_note(service):
    ticket_id = read_ticket_id()
    service.get(ticket_id)

    author = input("Enter your name: ").strip()
    message = input("Enter note (5–300 characters): ").strip()

    notes = service.add_note(ticket_id, author, message)
    print(f"Note added to ticket {ticket_id}.")

    if notes:
        note = notes[-1]
        print(f"{note['note_id']} | {note['author']}: {note['message']}")


def view_ticket_notes(service):
    ticket_id = read_ticket_id()
    notes = service.get_notes(ticket_id)

    if not notes:
        print(f"No notes found for ticket {ticket_id}.")
        return

    print(f"\n--- Notes for {ticket_id} ---")
    for note in notes:
        print(
            f"{note['note_id']} | {note['author']}: {note['message']}"
        )


def run_understanding_check(explanation_file=None):
    answers = []

    print("\n=== Engineering Understanding Check ===")
    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\n{number}. {question['question']}")
        for letter, option in question["options"].items():
            print(f"  {letter}. {option}")

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        while answer not in ("A", "B", "C", "D"):
            print("Invalid answer. Enter A, B, C, or D.")
            answer = input("Your answer (A/B/C/D): ").strip().upper()

        answers.append(answer)

    score = score_answers(answers)
    print(f"\nYour score: {score}/6")

    explanations = []
    for index in range(2):
        question_number = index + 1
        while True:
            explanation = input(
                f"Explain your reasoning for question {question_number}: "
            ).strip()
            if explanation:
                explanations.append(
                    f"Question {question_number}: "
                    f"{QUESTIONS[index]['question']}\n"
                    f"Answer selected: {answers[index]}\n"
                    f"Explanation: {explanation}\n"
                )
                break
            print("Please enter an explanation before continuing.")

    if explanation_file is None:
        explanation_file = (
            Path(__file__).parent / "data" / "quiz_explanations.txt"
        )
    explanation_file = Path(explanation_file)
    explanation_file.parent.mkdir(parents=True, exist_ok=True)
    with explanation_file.open("a", encoding="utf-8") as file:
        file.write("\n".join(explanations) + "\n")

    print(f"Explanations saved to {explanation_file}.")


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
        "9": ("View open work queue", lambda: list_unresolved(service)),
        "10": ("Generate report", lambda: show_report(service)),
        "11": (
            "Search tickets by title",
            lambda: search_tickets_by_title(service),
        ),
        "12": ("Add note to ticket", lambda: add_ticket_note(service)),
        "13": ("View ticket notes", lambda: view_ticket_notes(service)),
        "14": (
            "Search tickets sorted by priority",
            lambda: search_tickets_sorted(service),
        ),
        "15": ("Engineering Understanding Check", run_understanding_check),
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