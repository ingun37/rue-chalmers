import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import torch

from lib import Avatar, generate_avatar, save_avatar


class LibTests(unittest.TestCase):
    def test_generate_avatar_returns_avatar(self):
        model = Mock()
        with patch("lib.anny.Anny", return_value=model) as anny_model:
            avatar = generate_avatar(1)

        self.assertEqual(Avatar(seed=1), avatar)
        self.assertIs(model, avatar.model)
        anny_model.assert_called_once_with()

    def test_save_avatar_exports_glb(self):
        model = Mock()
        model.return_value = {
            "vertices": torch.tensor(
                [[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]]
            )
        }
        model.faces = torch.tensor([[0, 1, 2]])
        avatar = Avatar(seed=1, model=model)

        with tempfile.TemporaryDirectory() as temporary_directory:
            output_path = save_avatar(
                avatar, Path(temporary_directory) / "avatar-path"
            )

            self.assertEqual(".glb", output_path.suffix)
            self.assertTrue(output_path.is_file())

        model.assert_called_once_with()

    def test_save_avatar_requires_model(self):
        with self.assertRaisesRegex(ValueError, "does not contain an Anny model"):
            save_avatar(Avatar(seed=1), "avatar-path")


if __name__ == '__main__':
    unittest.main()
