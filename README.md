# CampusFlow — IT Helpdesk Ticket Manager

CampusFlow is a Python application for creating, prioritizing, assigning, and tracking IT helpdesk tickets.

## Project goals

- Create and validate tickets.
- Calculate ticket priority automatically.
- Assign tickets to support personnel.
- Track ticket status.
- Sort unresolved tickets by priority.
- Generate ticket reports.
- Save and load ticket data using JSON.
- Test the application with Python's unittest framework.

## Team responsibilities

- Person A: Ticket creation, validation, priority calculation, and related tests.
- Person B: Ticket assignment, workflow, unresolved queue, reports, and related tests.

Both team members must agree on shared function names and ticket data fields before integrating their work.

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
