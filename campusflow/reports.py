
def generate_report(tickets):
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be a list")

    by_status = {
        "open": 0,
        "in_progress": 0,
        "resolved": 0,
        "closed": 0,
    }

    by_priority = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
    }

    for ticket in tickets:
        if not isinstance(ticket, dict):
            raise ValueError("Each ticket must be a dictionary")

        status = ticket.get("status")
        priority = ticket.get("priority")

        if status not in by_status:
            raise ValueError("Invalid ticket status")

        if priority not in by_priority:
            raise ValueError("Invalid ticket priority")

        by_status[status] += 1
        by_priority[priority] += 1

    total_affected_users = sum(
        ticket.get("affected_users", 0) for ticket in tickets
    )

    closed_affected_users = sum(
        ticket.get("affected_users", 0)
        for ticket in tickets
        if ticket.get("status") == "closed"
    )

    return {
        "total": len(tickets),
        "by_status": by_status,
        "by_priority": by_priority,
        "total_affected_users": total_affected_users,
        "closed_affected_users": closed_affected_users,
    }

