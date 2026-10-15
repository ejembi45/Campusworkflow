# CampusFlow Next Baseline Check

## Feature verification

- [x] Search tickets by title.
- [x] Combine title, category, status, and priority filters.
- [x] Generate reports and handle an empty ticket list.
- [x] Add ticket notes through the CLI.
- [x] View ticket notes through the CLI.
- [x] Persist notes through JSON storage reloads.
- [x] Provide a six-question Engineering Understanding Check.
- [x] Accept only A/B/C/D quiz answers and retry invalid input.
- [x] Calculate a score out of six.
- [x] Save explanations for at least two quiz answers for mentor discussion.

## Automated tests

Run the complete suite with:

```bash
python3 -m unittest discover -s tests -v

Then update the AI learning log with what you actually implemented. First inspect its current content:

```bash
cat docs/ai-learning-log.md
- [x] Accept only A/B/C/D quiz answers and retry invalid input.
- [x] Calculate a score out of six.
- [x] Save explanations for at least two quiz answers for mentor discussion.

## Automated tests

Run the complete suite with:

    python3 -m unittest discover -s tests -v

Latest observed result during development: 114 tests ran. Confirm the final result before submitting.

## Manual checks still required

- [ ] Run the CLI and verify menu options 12, 13, and 14.
- [ ] Test invalid quiz input and confirm the program retries.
- [ ] Complete the quiz and verify the saved explanations file.
- [ ] Run the complete test suite again before submitting the pull request.
- [ ] Verify the integrated project on the intended repository after partner review and merge.
