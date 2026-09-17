import json
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from src.text_stats import calculate_stats, main


class TextStatsTests(unittest.TestCase):
    def test_calculate_stats(self):
        self.assertEqual(
            calculate_stats("Hello, world!\nCafé time."),
            {"lines": 2, "words": 4, "characters": 24},
        )

    def test_calculate_stats_empty_text(self):
        self.assertEqual(
            calculate_stats(""),
            {"lines": 0, "words": 0, "characters": 0},
        )

    def test_main_prints_json_for_utf8_file(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "input.txt"
            path.write_text("One café.\nTwo words.", encoding="utf-8")
            original_argv = sys.argv
            output = StringIO()
            try:
                sys.argv = ["text_stats.py", str(path)]
                with redirect_stdout(output):
                    main()
            finally:
                sys.argv = original_argv

        self.assertEqual(
            json.loads(output.getvalue()),
            {"lines": 2, "words": 4, "characters": 20},
        )


if __name__ == "__main__":
    unittest.main()
