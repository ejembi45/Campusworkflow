
# CampusFlow Next — Baseline Check

## 1. Purpose

This document records the original CampusFlow baseline and the verification tasks for CampusFlow Next.

The original baseline document was committed in Git commit `1a0166e` on 15 October 2026. The original baseline document is preserved at the repository root as `baseline-check.md`.

## 2. Historical Test Record

The original baseline document recorded this command:

```bash
python3 -m unittest discover -s test -v
```

Recorded result:

```text
Ran 99 test in 0.090s

OK
```

**Verification note:** The historical command uses `test`, but the repository contains a `tests/` directory. This historical result is preserved as recorded and is not presented as an independently verified result.

## 3. Independently Verified Baseline Test

The baseline parent commit was:

`f6c4d1fd85d7d63c0b5565b0eb11db77d0fbbcb6`

The original code at this commit was tested in a separate Git worktree using:

```bash
python3 -m unittest discover -s tests -v
```

Verified result:

```text
Ran 112 tests in 0.029s

OK
```

All 112 discovered tests passed during that independent verification. This is a historical baseline result, not the final CampusFlow Next test result.

## 4. Baseline Inputs and Observations

### Input 1: Valid Ticket Creation

**Input:** A ticket with a title, category, urgency, and number of affected users.

**Recorded observation:** The original baseline document reported that valid tickets could be created and their priority calculated.

### Input 2: Invalid Affected-User Values

**Input:** Invalid values for the number of affected users.

**Recorded observation:** The original baseline document reported that invalid values were rejected. This observation was retained from the historical record and was not independently reproduced during the test run in Section 3.

### Input 3: Ticket Workflow

**Input:** Ticket assignment and status transitions.

**Recorded observation:** The original baseline document reported that the application supported ticket assignment and workflow status changes.

These observations are retained from the original baseline record. They should not be interpreted as newly performed manual tests.

## 5. CampusFlow Next Feature Verification

Use this checklist to verify the new features before submission. Mark an item complete only after the relevant behaviour has actually been tested.

- [ ] Search tickets by title.
- [ ] Combine title, category, status, and priority filters.
- [ ] Generate reports and handle an empty ticket list.
- [ ] Add ticket notes through the CLI.
- [ ] View ticket notes through the CLI.
- [ ] Persist notes through JSON storage reloads.
- [ ] Provide a six-question Engineering Understanding Check.
- [ ] Accept only A/B/C/D quiz answers and retry invalid input.
- [ ] Calculate a score out of six.
- [ ] Save explanations for at least two quiz answers for mentor discussion.

## 6. Automated Test Verification

Run the complete test suite from the project root:

```bash
python3 -m unittest discover -s tests -v
```

Record the actual result from the final integrated version here:

- Test command: `python3 -m unittest discover -s tests -v`
- Number of tests run: To be recorded after execution.
- Result: To be recorded after execution.

Do not substitute historical test counts for the result of the final integrated version.

## 7. Manual Checks Still Required

- [ ] Run the CLI and verify menu options 12, 13, and 14.
- [ ] Test invalid quiz input and confirm the program retries.
- [ ] Complete the quiz and verify the saved explanations file.
- [ ] Run the complete test suite again before submitting the pull request.
- [ ] Verify the integrated project on the intended repository after partner review and merge.

## 8. Improvements Identified for CampusFlow Next

The baseline review identified these areas for implementation or stronger verification:

- Add follow-up notes to tickets.
- Validate note authors and messages.
- Generate note IDs independently for each ticket.
- Prevent notes from being added to resolved tickets.
- Validate persisted JSON data before replacing in-memory ticket data.
- Reject duplicate or malformed ticket and note data during loading.
- Preserve data when saving fails.
- Preserve ticket and note ID continuity after saving and reloading.
- Keep existing CampusFlow behaviour working while adding new features.

## 9. Evidence and Limitations

The historical 99-test result and the baseline observations were retained from the original baseline document. The 112-test result was independently verified at the baseline parent commit in a separate Git worktree.

The new feature checklist is a verification plan. Its unchecked items must not be treated as completed tests until evidence is collected.
