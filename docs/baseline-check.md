# CampusFlow Next Baseline Check

This file records the baseline behaviour observed before the CampusFlow Next
changes and the verification status of the integrated project.

## Baseline (old application)

The existing application was run and its tests executed before new work began.

Command:

    python3 -m unittest discover -s tests -v

Three inputs were exercised against the old application:

1. Create a valid ticket with title, category, urgency, and affected users.
   Observed: the ticket was created and its priority was calculated.
2. Enter an invalid affected-users value.
   Observed: the invalid value was rejected instead of creating a bad ticket.
3. Assign a ticket and change its status through the workflow.
   Observed: assignment and the existing status transitions worked.

The baseline review identified these improvements for CampusFlow Next:

- Add follow-up notes to tickets and validate author/message data.
- Generate note IDs per ticket and prevent notes on resolved tickets.
- Strengthen JSON validation before replacing in-memory data.
- Reject duplicate or malformed ticket and note data during loading.
- Preserve data when saving fails.
- Preserve ticket and note ID continuity after saving and reloading.
- Add combined search/filtering, richer reports, and a CLI understanding check.

## CampusFlow Next feature verification

- [x] Search tickets by title with case-insensitive substring matching.
- [x] Combine title, category, status, and priority filters (logical AND).
- [x] Re-prompt on an empty title and on invalid filter options.
- [x] View search results sorted by priority then numeric ticket ID.
- [x] Original Open Work Queue still lists only `open` tickets.
- [x] Generate reports with status, priority, and category counts.
- [x] Report unresolved/resolved counts and resolution percentage (0% when empty).
- [x] Add and view ticket notes through the CLI.
- [x] Persist notes through JSON storage reloads.
- [x] Provide a six-question Engineering Understanding Check.
- [x] Accept only A/B/C/D quiz answers and retry invalid input.
- [x] Calculate a score out of six and save two explanations for discussion.

## Automated tests

Run the complete suite from the project root:

    python3 -m unittest discover -s tests -v

Latest result after integration: **163 tests ran, OK**. The same command was
also run against a fresh clone of the repository with the same result.

## Manual checks still required

- [ ] Run the CLI and verify menu options 12 (add note), 13 (view notes),
      14 (sorted search), and 15 (understanding check).
- [ ] Test invalid quiz input and confirm the program retries.
- [ ] Complete the quiz and verify `data/quiz_explanations.txt`.
- [ ] Run the complete test suite again on the merged `main` before submitting.
- [ ] Verify the integrated project on the intended repository after partner
      review and merge.
