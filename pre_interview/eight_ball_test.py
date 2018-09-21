import unittest
from unittest.mock import patch
from eight_ball import MagicBall


class TestInput(unittest.TestCase):

    @patch('builtins.input', side_effect=['yes'])
    def test_replay_input_yes(self, mock):
        self.assertEqual(MagicBall().mock_replay_inputs(), 'yes')

    @patch('builtins.input', side_effect=['YES'])
    def test_replay_input_no_lowercase(self, mock):
        self.assertEqual(MagicBall().mock_replay_inputs(), 'yes')

    @patch('builtins.input', side_effect=['no'])
    def test_replay_input_no(self, mock):
        self.assertEqual(MagicBall().mock_replay_inputs(), 'no')

    @patch('builtins.input', side_effect=['No'])
    def test_replay_input_no_uppercase(self, mock):
        self.assertEqual(MagicBall().mock_replay_inputs(), 'no')


    @patch('__main__.MagicBall.replay')
    def test_question_func(self, mock):
        MagicBall().question()
        self.assertTrue(mock.called)


if __name__ == '__main__':
    unittest.main()
