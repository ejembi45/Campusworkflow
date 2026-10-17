QUESTIONS = [
    {
        "question": "What should happen when a ticket ID does not exist?",
        "options": {
            "A": "Create a ticket automatically",
            "B": "Report that the ticket was not found",
            "C": "Delete the other tickets",
            "D": "Return the first ticket",
        },
        "answer": "B",
    },
    {
        "question": "Why save ticket notes to JSON storage?",
        "options": {
            "A": "To make notes disappear after exit",
            "B": "To change every ticket's priority",
            "C": "To preserve notes when the application restarts",
            "D": "To prevent users from viewing notes",
        },
        "answer": "C",
    },
    {
        "question": "What does a combined filter do?",
        "options": {
            "A": "Matches tickets that satisfy all supplied filters",
            "B": "Deletes tickets that do not match",
            "C": "Returns only the newest ticket",
            "D": "Ignores the title filter",
        },
        "answer": "A",
    },
    {
        "question": "Why should a failed note save be handled safely?",
        "options": {
            "A": "To silently discard all tickets",
            "B": "To mark every ticket resolved",
            "C": "To skip all future validation",
            "D": "To avoid leaving an unsaved note in memory",
        },
        "answer": "D",
    },
    {
        "question": "What should the program do when a menu choice is invalid?",
        "options": {
            "A": "Exit immediately every time",
            "B": "Explain the choice is invalid and ask again",
            "C": "Run a random menu action",
            "D": "Clear the ticket storage",
        },
        "answer": "B",
    },
    {
        "question": "Why keep quiz scoring separate from displaying questions?",
        "options": {
            "A": "So the score can never be calculated",
            "B": "So invalid answers become correct",
            "C": "So scoring can be tested independently",
            "D": "So the question bank must be duplicated",
        },
        "answer": "C",
    },
]


def score_answers(answers):
    """Return the number of correct answers out of six."""
    if len(answers) != len(QUESTIONS):
        raise ValueError("Exactly six answers are required.")

    return sum(
        answer == question["answer"]
        for answer, question in zip(answers, QUESTIONS)
    )
