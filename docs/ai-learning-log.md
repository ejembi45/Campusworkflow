# CampusFlow AI Learning Log

## Purpose
We use AI tools to help us understand concepts, investigate errors, and improve our code. We remain responsible for understanding and testing the final implementation.

## Guidelines
- Do not submit code you cannot explain.
- Verify AI suggestions against the project requirements.
- Run tests before claiming that a feature works.
- Record important AI assistance honestly.
- Record actual errors, fixes, and test results.
- Do not invent learning experiences or test results.

## Learning Entry Template

**Date:**

**Team member:**

**Feature or task:**

**Problem or question:**

**What we asked AI:**

**What AI suggested:**

**What I learned in my own words:**

**What I implemented:**

**How I tested it:**

**Actual result:**

**What I can explain independently:**

**What I still need to learn:**

## Final Reflection
At the end of the project, each team member should explain what they learned about Python, testing, debugging, Git collaboration, and the use of AI.



## Learning Entry — Challenging and Correcting an AI Recommendation

**Date:** 10/10/2026.

**Team member:** IHWE MATHIAS ADE.

**Feature or task:** Automatic ticket ID generation and application startup.

**Problem or question:** I was working on automatic ticket ID generation and needed the application to start correctly and display its menu.

**What I asked AI:** I used AI assistance while working on this feature. I do not have the exact original prompt recorded in my notes.

**What AI suggested:** AI recommended an approach based on the fact that `service.py` was not explicitly listed in the project requirements. During the work, I noticed that `main.py` had been excluded from the proposed changes.

**What I learned in my own words:** I learned that I should not accept an AI recommendation just because it sounds reasonable. I need to run the application, observe what happens, and check whether the proposed solution addresses the actual problem.

**What I independently corrected or challenged:** I noticed that `main.py` had been excluded and insisted that AI address the omission rather than accepting the proposed approach without question.

**How I tested it:** I ran the application and waited for the expected menu to appear. After insisting on the correction, I ran it again to check the behaviour.

**Actual result:** The menu appeared and the application ran correctly after the correction.

**What I can explain independently:** I can explain what I expected to see when I ran the application, how I noticed the omission, why I challenged the AI recommendation, and how I checked the result by running the application again.

**What I still need to learn:** How to trace startup problems across `main.py` and supporting modules, and how to create automated tests that verify application startup and ticket ID generation.

**Reflection:** AI is a useful assistant, but it does not replace my responsibility to understand the project, question recommendations, test changes, and verify the outcome.

---

## Learning Entry 1 — Implementing and Verifying the Ticket Workflow

**Date:** 11/10/2026

**Team member:** Faith Ochanya Ejembi

**Feature or task:** Ticket status transitions and workflow validation.

**Problem or question:** I needed to make the ticket workflow follow the assignment rules, including how tickets move between statuses and when a resolved ticket can be changed.

**What I asked AI:** I used AI guidance to understand the workflow requirements, break them into smaller rules, and reason about how the implementation and tests should reflect those rules. This is a summary of the assistance, not a verbatim prompt.

**What AI suggested:** AI helped me reason about status transitions, assignment requirements, and the need to verify workflow behaviour against the specification.

**What I verified or corrected myself:** I compared the workflow implementation with the assignment requirements. I checked the handling of the `open`, `in_progress`, `resolved`, and `closed` statuses and considered the restrictions on unassigned tickets and changes to resolved tickets. I also reviewed the tests rather than relying only on the suggested implementation.

**What I implemented:** I contributed workflow and reporting changes on my `feature/workflow-reports` branch. My workflow-related work was committed and included in the merged project history.

**How I tested it:** I ran the relevant workflow tests during development. An earlier test run reported 24 tests passing; the integrated project was tested again later.

**Actual result:** The workflow and reporting contribution was integrated into `main`. The later integrated test run reported 84 tests passing.

**What I learned in my own words:** Requirements must be translated into explicit rules before implementing a workflow. A status change is not just assigning a new string; it must respect the allowed transitions and the ticket's current state.

**What I can explain independently:** I can explain why workflow transitions need validation and why tests should cover both permitted and prohibited changes.

**What I still need to learn:** How to design more comprehensive tests for every valid and invalid status transition.

---

## Learning Entry 2 — Checking Compatibility Between the Ticket Engine and Reports

**Date:** 11/10/2026

**Team member:** Faith Ochanya Ejembi

**Feature or task:** Integrating ticket workflow and reporting with the ticket engine.

**Problem or question:** The ticket engine and workflow/reporting code needed to agree on ticket IDs and ticket data. If these components used different assumptions, ticket lookup, ordering, or reports could behave incorrectly.

**What I asked AI:** I used AI assistance to understand the integration requirements and reason about how ticket IDs and workflow/reporting behaviour should remain consistent. This describes the assistance in summary; I do not have a verbatim prompt recorded.

**What AI suggested:** AI helped me examine the relationship between the ticket engine, workflow, reports, and tests, including the importance of using consistent ticket ID conventions.

**What I verified or corrected myself:** I reviewed the project requirements and Git changes. I checked that the integrated project used the required `T`-prefixed ticket IDs, such as `T001`, and that ordering should use the numeric part of an ID rather than treating the whole ID as an arbitrary string. I also checked the repository history to confirm that the integration reached `main`.

**What I implemented:** I worked on workflow and reporting compatibility with the ticket engine. The ticket-engine implementation was also contributed by my teammate, so I do not claim that work as mine alone.

**How I tested it:** I ran the integrated test suite and checked the Git history after updating my branch from `origin/main`.

**Actual result:** The merged project contained the ticket-engine and workflow/reporting changes. The integrated test run reported 84 tests passing.

**What I learned in my own words:** Separate modules must agree on shared data formats and assumptions. A feature can work in isolation but still fail when connected to another module, so integration checks are important.

**What I can explain independently:** I can explain why consistent IDs matter for finding tickets and why numeric ordering matters when IDs contain letters and numbers.

**What I still need to learn:** How to create focused integration tests that detect mismatches between modules before merging.

---

## Learning Entry 3 — Verifying Tests, Commits, and Branch Integration

**Date:** 11/10/2026

**Team member:** Faith Ochanya Ejembi

**Feature or task:** Testing the integrated project and verifying Git history.

**Problem or question:** After the workflow and ticket-engine changes were merged, I needed to confirm that my local project was up to date and that the integrated tests passed.

**What I asked AI:** I asked AI for step-by-step guidance on checking the repository state, updating my branch from `main`, and understanding the test output. This is a summary rather than an exact quotation of the prompts.

**What AI suggested:** AI guided me through using Git status and history commands and running Python's unittest discovery against the `tests` directory.

**What I verified or corrected myself:** I ran the commands in my Ubuntu terminal. I checked the branch status and Git history, fetched updates from `origin`, merged `origin/main` into my feature branch, and confirmed that my branch was up to date with its remote. I also inspected the actual test output rather than assuming that the tests had passed.

**What I implemented:** I updated my working branch with the merged project and pushed the branch update to its remote.

**How I tested it:** I ran:

`python3 -m unittest discover -s tests -v`

I checked the terminal output for the test count and final status.

**Actual result:** The integrated test run reported `Ran 84 tests` followed by `OK`. Git also confirmed that my workflow-related commit was included in the history of `origin/main`.

**What I learned in my own words:** Git commands provide evidence about which branch I am on and which commits it contains. Likewise, a test result is useful only when I actually run the tests and inspect the result. Passing tests give confidence in covered behaviour but do not prove that every possible case is correct.

**What I can explain independently:** I can explain the purpose of `git fetch`, `git merge`, `git status`, Git history, and `python3 -m unittest discover -s tests -v`.

**What I still need to learn:** How to write stronger edge-case tests and use continuous integration to run the test suite automatically on pull requests.

---


## Learning Entry — Engineer A: Follow-up Notes, Safe Storage, and Testing

**Date:** 15/10/2026

**Team member:** EJEMBI EDWIN

**Feature or task:** CampusFlow Next — Engineer A follow-up notes, validation, JSON storage safety, and testing.

**Problem or question:** I needed to implement the Engineer A requirements without breaking the existing CampusFlow application. My work included follow-up notes, note validation, safe JSON loading and saving, preserving existing ticket workflow behaviour, and making sure note IDs continue correctly after data is reloaded.

**What I asked AI:** I used AI as a step-by-step guide to understand the existing code, interpret the CampusFlow Next requirements, reason about validation and mutation safety, write and review tests, understand test failures, and work through Git and merge conflicts.

**What AI suggested:** AI helped me break the requirements into smaller rules. This included validating data before changing the ticket collection, validating note authors and messages, generating note IDs per ticket, preventing notes on resolved tickets, testing persistence after JSON reload, and verifying changes with the full test suite.

**What I verified or corrected myself:** I ran the commands and tests myself and checked the actual results. I also checked Git status and diffs before committing changes. When code was accidentally placed in the wrong test file, I identified the changed file using `git status`, restored it, opened the correct file, and tested again before committing.

**What I implemented:** I contributed the `notes` field to tickets, follow-up note creation, note validation, per-ticket note ID generation, restrictions on adding notes to resolved tickets, safe JSON validation/loading behaviour, rollback protection for failed saves, the service-layer `add_note` method, and tests for the Engineer A functionality. I also added the CampusFlow Next baseline check.

**How I tested it:** I ran focused storage tests with:

`python3 -m unittest tests.test_storage -v`

The storage test suite reported 39 tests passing.

I then ran the complete project test suite with:

`python3 -m unittest discover -s tests -v`

**Actual result:** The complete project reported `Ran 113 tests` followed by `OK`. The new persistence test also confirmed that notes survive a JSON reload and that the next note ID continues from `N001` to `N002`.

**What I learned in my own words:** I learned that validation should happen before mutation. If invalid data changes memory before it is rejected, the application can be left in an incorrect state. I also learned that saving data safely requires thinking about both the JSON file and the in-memory data. For notes, I learned why IDs should be generated from the existing notes for that ticket and why a rejected note must not consume an ID.

I also learned more about Git collaboration. A merge conflict does not mean choosing one person's entire file over another person's file. I need to understand both changes and preserve the correct parts of each contribution. During the merge, I preserved my follow-up note functionality together with my teammate's existing changes.

**What I can explain independently:** I can explain why notes are allowed only on appropriate ticket statuses, how note IDs such as `N001` and `N002` are generated, why validation happens before mutation, why `type(value) is int` can be important when booleans must be rejected, how JSON data is validated before replacing the current ticket collection, why rollback is needed when saving fails, and how the tests verify these behaviours.

**What I still need to learn:** I want to improve my ability to design validation and persistence code independently, write more edge-case tests without assistance, and become more confident resolving larger Git merge conflicts.

**Reflection:** AI helped me understand the requirements and work through problems, but I verified the work by reading the code, running the tests, checking Git changes, correcting mistakes, and confirming the actual results before committing and pushing them.

---

> **Draft note (Engineer B):** the entries below describe events that really
> happened in this repository. Replace the bracketed fields with your own exact
> wording before submitting, and delete this note.

## Learning Entry — Engineer B: Agreeing the `add_note` contract

**Date:** 15/10/2026

**Team member:** Faith Ejembi

**Feature or task:** Integrating follow-up notes between the data layer
(Engineer A) and the CLI (Engineer B).

**Problem or question:** My `add_note` and my teammate's both "worked", but
they returned different things: mine returned the ticket's whole notes list,
his returned only the new note. When I merged `main` into my branch, five tests
failed and CLI options 12 and 13 crashed, even though each half had passed its
own tests.

**What we asked AI:** I asked AI to explain how a merge can fail when both
branches passed their own tests, and to help me list every caller of `add_note`
before choosing one fix.

**What AI suggested:** List each function's return-value contract and every
call site, choose a single contract, and update all callers and tests together.
It pointed out that "my tests pass" only means the tests of one branch pass.

**What I verified or corrected myself:** I used `git show HEAD:...` and
`git diff` to compare my version with my teammate's. I confirmed that
`main.py` used `notes[-1]` and that `service.get_notes` called
`storage.get_notes`, which did not exist. I chose the list contract, restored
`get_notes`, and updated the callers and tests.

**What I implemented:** The shared interface `add_note(...) -> list[note]` with
`get_notes(...) -> list[note]`, the reconciliation of `storage.py` and
`service.py`, and the updated tests in `test_notes.py`, `test_service.py`, and
`test_storage.py`.

**How I tested it:** `python3 -m unittest discover -s tests -v` reported 163
tests OK, and I ran the same command against a fresh clone with the same result.

**Actual result:** The merged project runs and the whole suite passes.

**What I can explain independently:** Why a shared function contract must be
agreed before integration, and why a passing suite on one branch does not prove
the integrated project is correct.

**What I still need to learn:** How to write a focused integration test that
would have caught this mismatch before the merge.

**Reflection:** [Explain, in your own words, what you believed before, what
changed, and how you would prevent this next time.]

## Learning Entry — Engineer B: `casefold`, punctuation, and substring search

**Date:** 15/10/2026

**Team member:** [Your full name]

**Feature or task:** Case-insensitive title search.

**Problem or question:** I wrote a search test with the title "Campus Wi-Fi
down" and searched for "wifi". It failed. I expected case-insensitive matching
to cover it, but "wi-fi" does not contain the characters "wifi".

**What we asked AI:** I asked AI to explain the difference between `casefold`
and `lower`, and what substring matching does and does not promise.

**What AI suggested:** `casefold` is the more aggressive, Unicode-friendly
normalization. Substring matching compares exact character sequences, so
punctuation and spaces must match. It suggested test cases but left the
implementation to me.

**What I verified or corrected myself:** I ran a small Python experiment:
`"wifi" in "Wi-Fi".casefold()` returned `False`, while `"wi-fi" in
"Wi-Fi".casefold()` returned `True`. I corrected my test fixture to use
consistent spelling and kept the matching rule as plain substring search.

**What I implemented:** `campusflow/search.py` `filter_tickets` with
case-insensitive substring matching, and `tests/test_search.py` covering case
insensitivity and punctuation.

**How I tested it:** `python3 -m unittest tests.test_search -v`, then the full
suite (163 tests OK).

**Actual result:** Search matches "WiFi", "wifi", and "WIFI" against the same
text, and does not pretend to do fuzzy spelling correction.

**What I can explain independently:** Why `casefold` is preferred for
case-insensitive comparison and why punctuation must match in a substring
search.

**What I still need to learn:** How to decide when simple substring search is
good enough versus when tokenization or normalization is needed.

**Reflection:** [Explain, in your own words, how the failing test changed the
way you think about "case-insensitive" matching.]

---