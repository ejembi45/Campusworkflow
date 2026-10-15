"""Read-only search, filtering and sorting helpers (Engineer B).

Every function in this module works on the ticket collection it is given
and never mutates it. Keeping this logic out of the CLI makes it possible
to test search behaviour without typing into ``input()``.
"""

PRIORITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

VALID_CATEGORIES = ("Network", "Hardware", "Software", "Other")
VALID_STATUSES = ("open", "in_progress", "resolved", "closed")
VALID_PRIORITIES = ("critical", "high", "medium", "low")


def filter_tickets(
    tickets,
    title=None,
    category=None,
    status=None,
    priority=None,
    assigned_to=None,
):
    """Return the tickets that match *every* supplied filter (logical AND).

    A filter value of ``None`` means "do not filter by this field".
    Title matching is a case-insensitive substring search.
    """
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be a list")

    results = list(tickets)

    if title is not None:
        search_text = title.casefold()
        results = [
            ticket
            for ticket in results
            if search_text in ticket["title"].casefold()
        ]

    if category is not None:
        results = [
            ticket for ticket in results
            if ticket["category"] == category
        ]

    if status is not None:
        results = [
            ticket for ticket in results
            if ticket["status"] == status
        ]

    if priority is not None:
        results = [
            ticket for ticket in results
            if ticket["priority"] == priority
        ]

    if assigned_to is not None:
        results = [
            ticket for ticket in results
            if ticket["assigned_to"] == assigned_to
        ]

    return results


def sort_by_priority(tickets):
    """Return tickets ordered by priority, then by numeric ticket ID.

    Priority order is critical > high > medium > low. Tickets that share a
    priority are ordered by the numeric part of their ID, so ``T002`` comes
    before ``T010`` (a plain string sort would get this wrong).
    """
    return sorted(
        tickets,
        key=lambda ticket: (
            PRIORITY_ORDER[ticket["priority"]],
            int(ticket["id"][1:]),
        ),
    )
