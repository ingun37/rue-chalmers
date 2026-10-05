import argparse
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main
from lib import Avatar


class MainTests(unittest.TestCase):
    def test_positive_int_accepts_positive_numbers(self):
        self.assertEqual(3, main.positive_int("3"))

    def test_positive_int_rejects_non_positive_numbers(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            main.positive_int("0")

    def test_run_collects_then_saves_avatars(self):
        generated = [Avatar(seed=10), Avatar(seed=11)]

        with tempfile.TemporaryDirectory() as temporary_directory:
            out_dir = Path(temporary_directory) / "nested" / "avatars"
            with (
                patch("main.generate_avatar", side_effect=generated) as generate_avatar,
                patch("main.save_avatar") as save_avatar,
            ):
                avatars = main.run(2, out_dir)

            self.assertEqual(generated, avatars)
            self.assertTrue(out_dir.is_dir())
            generate_avatar.assert_any_call(0)
            generate_avatar.assert_any_call(1)
            self.assertEqual(2, save_avatar.call_count)

            saved_paths = [call.args[1] for call in save_avatar.call_args_list]
            self.assertEqual(2, len(set(saved_paths)))
            self.assertTrue(all(path.parent == out_dir for path in saved_paths))
            self.assertTrue(all(path.suffix == "" for path in saved_paths))


if __name__ == '__main__':
    unittest.main()
