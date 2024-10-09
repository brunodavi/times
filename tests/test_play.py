from unittest import TestCase
from unittest.mock import patch, MagicMock

from times.lib import play


class TestPlay(TestCase):
    @patch('times.lib.playsound')
    def test_play_sound(self, playsound_mock: MagicMock):
        play('focus.mp3')

        self.assertIn('times/assets/focus.mp3', playsound_mock.call_args[0][0])
