import unittest

from campusflow.search import (
    PRIORITY_ORDER,
    filter_tickets,
    sort_by_priority,
)


def make_ticket(
    ticket_id,
    title,
    category="Network",
    priority="high",
    status="open",
    assigned_to=None,
):
    return {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": "high",
        "affected_users": 5,
        "priority": priority,
        "status": status,
        "assigned_to": assigned_to,
    }


class TestFilterTickets(unittest.TestCase):
    def setUp(self):
        self.tickets = [
            make_ticket("T001", "Campus wifi down", "Network", "critical"),
            make_ticket("T002", "Wifi login failure", "Software", "medium"),
            make_ticket(
                "T003",
                "Printer broken",
                "Hardware",
                "low",
                status="closed",
            ),
        ]

    def test_title_match_is_case_insensitive_substring(self):
        result = filter_tickets(self.tickets, title="WiFi")

        self.assertEqual([ticket["id"] for ticket in result], ["T001", "T002"])

    def test_empty_filters_return_every_ticket(self):
        self.assertEqual(filter_tickets(self.tickets), self.tickets)

    def test_combined_filters_use_and(self):
        result = filter_tickets(
            self.tickets,
            title="wifi",
            category="Network",
            status="open",
        )

        self.assertEqual([ticket["id"] for ticket in result], ["T001"])

    def test_filter_by_priority(self):
        result = filter_tickets(self.tickets, priority="low")

        self.assertEqual([ticket["id"] for ticket in result], ["T003"])

    def test_filter_by_assigned_to(self):
        tickets = self.tickets + [
            make_ticket("T004", "Router reboot", assigned_to="Ada")
        ]

        result = filter_tickets(tickets, assigned_to="Ada")

        self.assertEqual([ticket["id"] for ticket in result], ["T004"])

    def test_conflicting_filters_return_no_matches(self):
        result = filter_tickets(
            self.tickets,
            title="wifi",
            category="Hardware",
        )

        self.assertEqual(result, [])

    def test_filter_does_not_modify_input(self):
        snapshot = [dict(ticket) for ticket in self.tickets]

        filter_tickets(self.tickets, title="wifi", status="open")

        self.assertEqual(self.tickets, snapshot)

    def test_rejects_non_list_input(self):
        with self.assertRaises(ValueError):
            filter_tickets({"id": "T001"})


class TestSortByPriority(unittest.TestCase):
    def setUp(self):
        self.tickets = [
            make_ticket("T010", "low task", priority="low"),
            make_ticket("T002", "medium task", priority="medium"),
            make_ticket("T007", "critical task", priority="critical"),
            make_ticket("T003", "high task", priority="high"),
        ]

    def test_sorted_by_priority_order(self):
        result = sort_by_priority(self.tickets)

        self.assertEqual(
            [ticket["priority"] for ticket in result],
            ["critical", "high", "medium", "low"],
        )

    def test_ties_are_broken_by_numeric_ticket_id(self):
        tickets = [
            make_ticket("T010", "second", priority="high"),
            make_ticket("T002", "first", priority="high"),
        ]

        result = sort_by_priority(tickets)

        self.assertEqual([ticket["id"] for ticket in result], ["T002", "T010"])

    def test_sort_does_not_modify_input(self):
        snapshot = list(self.tickets)

        sort_by_priority(self.tickets)

        self.assertEqual(self.tickets, snapshot)

    def test_priority_order_constant(self):
        self.assertEqual(
            PRIORITY_ORDER,
            {"critical": 0, "high": 1, "medium": 2, "low": 3},
        )


if __name__ == "__main__":
    unittest.main()
