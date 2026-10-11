import re

VALID_CATEGORIES = ("Network", "Hardware", "Software", "Other")


def calculate_priority(urgency, affected_users):
    if not isinstance(urgency, str) or urgency not in ("high", "medium", "low"):
        raise ValueError("Invalid urgency")

    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError("affected_users must be a positive integer")

    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"


def create_ticket(ticket_id, title, category, urgency, affected_users):
    if not isinstance(ticket_id, str) or not re.fullmatch(r"T\d{3,}", ticket_id):
        raise ValueError("ticket_id must use the format T001")

    if not isinstance(title, str) or not title.strip():
        raise ValueError("title must be a non-empty string")

    if not isinstance(category, str) or not category.strip():
        raise ValueError("category must be a non-empty string")

    normalized_category = category.strip().lower()
    approved_categories = {
        item.lower(): item for item in VALID_CATEGORIES
    }

    if normalized_category not in approved_categories:
        raise ValueError(
            "Invalid category. Choose Network, Hardware, Software, or Other."
        )

    ticket = {
        "id": ticket_id,
        "title": title,
        "category": approved_categories[normalized_category],
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "status": "open",
        "assigned_to": None,
    }

    return ticket
