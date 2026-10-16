# CampusFlow Next — Baseline Check

## 1. Purpose

This document records the baseline state of CampusFlow before the CampusFlow Next changes. The original baseline document was committed in Git commit `1a0166e` on 15 October 2026.

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

**Verification note:** The historical command uses `test`, but the baseline repository contains a `tests/` directory. Therefore, the historical result is preserved as originally recorded rather than presented as the independently verified result.

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

All 112 discovered tests passed during this independent verification.

## 4. Baseline Inputs and Observations

### Input 1: Valid Ticket Creation

**Input:** A ticket with a title, category, urgency, and number of affected users.

**Recorded observation:** The original baseline document reported that valid tickets could be created and their priority calculated.

### Input 2: Invalid Affected-User Values

**Input:** Invalid values for the number of affected users.

**Recorded observation:** The original baseline document reported that invalid values were rejected. This observation is retained from the historical record and was not independently reproduced as part of the test run in Section 3.

### Input 3: Ticket Workflow

**Input:** Ticket assignment and status transitions.

**Recorded observation:** The original baseline document reported that the existing application supported ticket assignment and workflow status changes.

These three observations are retained from the original baseline record; they should not be interpreted as three newly performed manual tests.

## 5. Improvements Identified for CampusFlow Next

The baseline review identified the following areas for implementation or stronger verification:

- Add follow-up notes to tickets.
- Validate note authors and messages.
- Generate note IDs independently for each ticket.
- Prevent notes from being added to resolved tickets.
- Validate persisted JSON data before replacing in-memory ticket data.
- Reject duplicate or malformed ticket and note data during loading.
- Preserve data when saving fails.
- Preserve ticket and note ID continuity after saving and reloading.
- Keep existing CampusFlow behaviour working while adding new features.

## 6. Evidence and Limitations

The original baseline document remains at the repository root as `baseline-check.md`. This document provides the assessment copy under `docs/baseline-check.md`.

The 99-test result and the three baseline observations come from the historical document. The 112-test result was independently verified at the baseline parent commit in a separate Git worktree.
