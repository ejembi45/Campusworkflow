import unittest

from campusflow.reports import generate_report
from campusflow.service import TicketService
from campusflow.storage import TicketStorage


class TestReports(unittest.TestCase):
    def test_empty_report_resolution_percentage_is_zero(self):
        report = generate_report([])

        self.assertEqual(report["resolution_percentage"], 0)

    def test_empty_report_counts_are_zero(self):
        report = generate_report([])

        self.assertEqual(report["unresolved_count"], 0)
        self.assertEqual(report["resolved_count"], 0)
        self.assertEqual(report["total"], 0)

    def test_counts_follow_current_status_after_resolve_and_reopen(self):
        service = TicketService(TicketStorage())
        service.create("T001", "Wi-Fi down", "Network", "high", 15)
        service.assign("T001", "Ada")
        service.start("T001")
        service.resolve("T001")

        resolved = generate_report(service.get_all())
        self.assertEqual(resolved["resolved_count"], 1)
        self.assertEqual(resolved["unresolved_count"], 0)
        self.assertEqual(resolved["resolution_percentage"], 100.0)

        service.reopen("T001")

        reopened = generate_report(service.get_all())
        self.assertEqual(reopened["resolved_count"], 0)
        self.assertEqual(reopened["unresolved_count"], 1)
        self.assertEqual(reopened["resolution_percentage"], 0)

    def test_categories_are_counted_once(self):
        service = TicketService(TicketStorage())
        service.create("T001", "Wi-Fi down", "Network", "high", 15)
        service.create("T002", "Printer broken", "Hardware", "low", 1)

        report = generate_report(service.get_all())

        self.assertEqual(report["total"], 2)
        self.assertEqual(report["by_category"]["Network"], 1)
        self.assertEqual(report["by_category"]["Hardware"], 1)

    def test_status_counts_do_not_overlap(self):
        tickets = [
            {"category": "Network", "priority": "high", "status": "open",
             "affected_users": 1},
            {"category": "Network", "priority": "high", "status": "in_progress",
             "affected_users": 1},
            {"category": "Network", "priority": "high", "status": "resolved",
             "affected_users": 1},
            {"category": "Network", "priority": "high", "status": "closed",
             "affected_users": 1},
        ]

        report = generate_report(tickets)

        self.assertEqual(report["total"], 4)
        self.assertEqual(sum(report["by_status"].values()), 4)


if __name__ == "__main__":
    unittest.main()
