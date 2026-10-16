# CampusFlow — IT Helpdesk Ticket Manager

CampusFlow is a Python application for creating, prioritizing, assigning, and tracking IT helpdesk tickets.
## Project goals

- Create and validate IT helpdesk tickets.
- Calculate ticket priority automatically.
- Assign tickets to support personnel.
- Protect valid ticket status transitions.
- Prevent unassigned tickets from moving to `in_progress`.
- Add follow-up notes to `open` and `in_progress` tickets.
- Validate note authors and messages.
- Generate per-ticket note IDs such as `N001` and `N002`.
- Search and filter tickets.
- Sort the open work queue by priority and ticket ID.
- Generate ticket reports and analytics.
- Save and load ticket data safely using JSON.
- Validate saved data before replacing in-memory data.
- Test the application with Python's `unittest` framework.

## Team responsibilities

### Engineer A
Engineer A is responsible for:
- Validation helpers and data integrity.
- Assignment and status mutation protections.
- Follow-up note data validation.
- JSON save/load safety and ID continuity.
- Business/data-layer note functionality.
- The `add_note` service operation.
- Engineer A tests.

### Engineer B
Engineer B is responsible for:
- CLI follow-up note interaction and display.
- Ticket search and filtering UI.
- Reports and analytics.
- Engineer B tests.

Both engineers must coordinate shared interfaces and preserve existing CampusFlow behaviour while integrating CampusFlow Next features.

## Run tests

Run the following command from the project root:

    python3 -m unittest discover -s tests -v

## Project status

The project is under development. Features will be marked complete only after implementation and testing.

## Ticket IDs

Each ticket has a unique string ID consisting of `T` followed by at least
three digits, such as `T001`, `T002`, and `T003`. New tickets receive the
next available numeric ID. Existing saved tickets retain their IDs during
normal application use.

## Follow-up notes

Tickets contain a `notes` list for recording follow-up information.

Each note contains:
- `note_id`
- `author`
- `message`

Note IDs are generated independently for each ticket using IDs such as `N001`, `N002`, and `N003`.

Notes can only be added while a ticket is `open` or `in_progress`. A resolved ticket must be reopened before another note can be added.

The note author must not be blank. The note message is trimmed and must contain between 5 and 300 characters.

Saved notes are preserved in JSON and their ID sequence continues correctly after the application reloads.