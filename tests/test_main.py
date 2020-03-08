import unittest
from main import Program
from error_messages import Error, Notice
from song import Song
from mock import patch, call


class TestMain(unittest.TestCase):

    def setUp(self):
        """Initialise program and register two songs before each test."""

        self.program = Program()
        self.program.song_dict = {}
        self.program.song_dict['A'] = Song('A', 1)
        self.program.song_dict['B'] = Song('B', 2)
        self.program.song_dict['Z'] = Song('Z', 3)

    @patch('sys.stdout')
    @patch('main.Program._print_results')
    def assert_correct_print(self, do_something, inputs, expected_messages,
                             mock_print_results, mock_print):
        """Assert that correct print statements are made in tests."""

        for i in range(len(inputs)):
            with self.subTest(input=inputs[i]):
                mock_print.mock_calls = []
                do_something(inputs[i])
                if expected_messages[i] is None:
                    expected = []
                else:
                    expected = [call.write(expected_messages[i]),
                                call.write('\n')]
                actual = mock_print.mock_calls
                self.assertEqual(actual, expected)

    def test_do_song(self):
        # NOTE: Negative ratings are allowed in this test
        inputs = ['C', ' D ', 'E 2', 'F F', 'G 2 3',
                  'H     2', 'I 0', 'J -3', ' ', '  ', '   ', 'A A', 'A 1']
        expected_messages = [Error.song_syntax, Error.song_syntax, None,
                             Error.invalid_rating, Error.song_syntax,
                             Error.song_syntax, None, None, Error.song_syntax,
                             Error.song_syntax, Error.song_syntax,
                             Error.invalid_rating, Notice.rating_updated('A', 1)]

        self.assert_correct_print(
            self.program.do_song, inputs, expected_messages)

    def test_do_similar(self):
        inputs = ['A A', 'A B', 'A    B', ' ', '  ', 'C D', 'A C', 'C A']
        expected_messages = [Error.same_song, None, Error.similarity_syntax,
                             Error.similarity_syntax, Error.similarity_syntax,
                             Error.neither_song_registered,
                             Error.song_b_not_registered,
                             Error.song_a_not_registered]

        self.assert_correct_print(
            self.program.do_similar, inputs, expected_messages)

    def test_do_get_song_matches(self):
        inputs = ['', 'A A', 'A', 'A 1', 'B 0',
                  'B -1', 'A   2', ' ', 'C 3', 'A 1.1']
        expected_messages = [Error.matches_syntax, Error.matches_syntax,
                             Error.matches_syntax, None, None,
                             Error.invalid_num_matches, Error.matches_syntax,
                             Error.matches_syntax,
                             Error.matches_song_not_registered,
                             Error.invalid_num_matches]

        self.assert_correct_print(
            self.program.do_get_song_matches, inputs, expected_messages)

    @patch('main.Program._confirm_response')
    def test_remove_all_similarities(self, mock_confirmation):
        mock_confirmation.return_value = True
        self.program.song_dict['A'].add_similar_song(self.program.song_dict['B'])
        self.program.song_dict['A'].add_similar_song(self.program.song_dict['Z'])
        self.program.song_dict['B'].add_similar_song(self.program.song_dict['Z'])
        self.program.do_remove_all_similarities('')
        self.assertEqual(self.program.song_dict['A'].similar_songs, [])
        self.assertEqual(self.program.song_dict['B'].similar_songs, [])
        self.assertEqual(self.program.song_dict['Z'].similar_songs, [])
