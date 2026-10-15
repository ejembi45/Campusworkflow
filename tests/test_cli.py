import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main as main_module
from campusflow.quiz import QUESTIONS, score_answers
from campusflow.service import TicketService
from campusflow.storage import TicketStorage


class TestPromptFilter(unittest.TestCase):
    def test_reprompts_until_a_valid_option_is_given(self):
        with patch("builtins.input", side_effect=["nope", "network"]):
            with patch("builtins.print"):
                result = main_module.prompt_filter(
                    "Category",
                    ("Network", "Hardware"),
                )

        self.assertEqual(result, "Network")

    def test_blank_input_returns_none(self):
        with patch("builtins.input", side_effect=[""]):
            result = main_module.prompt_filter("Status", ("open",))

        self.assertIsNone(result)


class TestCollectSearch(unittest.TestCase):
    def setUp(self):
        self.service = TicketService(TicketStorage())

    def test_empty_title_reprompts(self):
        inputs = ["", "wifi", "", "", ""]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as printed:
                title, _ = main_module.collect_search(self.service)

        messages = " ".join(str(call) for call in printed.call_args_list)
        self.assertEqual(title, "wifi")
        self.assertIn("Search title cannot be empty.", messages)

    def test_invalid_filter_reprompts(self):
        inputs = ["printer", "bogus", "Hardware", "", ""]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as printed:
                main_module.collect_search(self.service)

        messages = " ".join(str(call) for call in printed.call_args_list)
        self.assertIn("Invalid category", messages)


class TestUnderstandingCheck(unittest.TestCase):
    def answers(self):
        return [question["answer"] for question in QUESTIONS]

    def test_rejects_invalid_answer_then_scores_correctly(self):
        correct = self.answers()
        # First attempt for question 1 is invalid, then the correct answer.
        inputs = ["Z", correct[0]] + correct[1:] + ["reason one", "reason two"]

        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "explanations.txt"

            with patch("builtins.input", side_effect=inputs):
                with patch("builtins.print"):
                    main_module.run_understanding_check(output)

            saved = output.read_text(encoding="utf-8")

        self.assertIn("Question 1", saved)
        self.assertIn("Question 2", saved)
        self.assertEqual(score_answers(correct), 6)

    def test_prints_score_out_of_six(self):
        inputs = self.answers() + ["reason one", "reason two"]

        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "explanations.txt"

            with patch("builtins.input", side_effect=inputs):
                with patch("builtins.print") as printed:
                    main_module.run_understanding_check(output)

        messages = " ".join(str(call) for call in printed.call_args_list)
        self.assertIn("6/6", messages)


class TestMenu(unittest.TestCase):
    def test_invalid_choice_is_reported_before_exit(self):
        with patch("builtins.input", side_effect=["99", "0"]):
            with patch("builtins.print") as printed:
                main_module.main()

        messages = " ".join(str(call) for call in printed.call_args_list)
        self.assertIn("Invalid option", messages)


if __name__ == "__main__":
    unittest.main()
