import re

VALID_CATEGORIES = ("Network", "Hardware", "Software", "Other")


def calculate_priority(urgency, affected_users):
    urgency = urgency.strip().lower() if isinstance(urgency, str) else urgency

    if not isinstance(urgency, str) or urgency not in ("high", "medium", "low"):
        raise ValueError("Urgency must be high, medium, or low")

    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError("Affected users must be a positive integer")

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
        raise ValueError("Title is required")

    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must be Network, Hardware, Software, or Other")

    category_names = {item.lower(): item for item in VALID_CATEGORIES}
    normalized_category = category.strip().lower()

    if normalized_category not in category_names:
        raise ValueError("Category must be Network, Hardware, Software, or Other")

    normalized_urgency = urgency.strip().lower() if isinstance(urgency, str) else urgency

    ticket = {
        "id": ticket_id,
        "title": title.strip(),
        "category": category_names[normalized_category],
        "urgency": normalized_urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(normalized_urgency, affected_users),
        "status": "open",
        "assigned_to": None,
    }

    return ticket
