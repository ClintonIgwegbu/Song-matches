from sys import path  # TODO Where is the recursion error coming from here?
path.insert(0, 'src')
import unittest
from main import Program
from error_messages import Error
from song import Song
from mock import patch, call, MagicMock

class TestMain(unittest.TestCase):
    # These methods take input from the user, so definitely do need to be tested

    def setUp(self):
        self.program = Program()
        self.mock_print = MagicMock()  # Allows tests to keep track of calls to print
        self.mock_print_results = MagicMock()
        self.program.song_dict = {}
        self.program.song_dict['A'] = Song('A', 1)
        self.program.song_dict['B'] = Song('B', 2)

    def assert_correct_print(self, do_something, inputs, expected_messages):
        with patch('sys.stdout', self.mock_print):
            with patch('main.Program._print_results', self.mock_print_results):
                for i in range(len(inputs)):
                    with self.subTest(input=inputs[i]):
                        self.mock_print.mock_calls = []
                        do_something(inputs[i])
                        if expected_messages[i] == None:
                            expected = []
                        else:
                            expected = [call.write(expected_messages[i]), call.write('\n')]
                        actual = self.mock_print.mock_calls
                        self.assertEqual(actual, expected)

    # NOTE: Negative ratings are allowed in this test
    def test_do_song(self):
        inputs = ['A', ' A ', 'A 2', 'A A', 'A 2 3', 'A     2', 'A 0', 'A -3', ' ', '  ', '   ']
        expected_messages = [Error.song_syntax, Error.song_syntax, None, Error.invalid_rating, Error.song_syntax, Error.song_syntax, None, None, Error.song_syntax, Error.song_syntax, Error.song_syntax]
        self.assert_correct_print(self.program.do_song, inputs, expected_messages)

    def test_do_similar(self):
        inputs = ['A A', 'A B', 'A    B', ' ', '  ', 'C D', 'A C', 'C A']
        expected_messages = [Error.same_song, None, Error.similarity_syntax, Error.similarity_syntax, 
        Error.similarity_syntax, Error.similarity_neither_song_registered, Error.similarity_song_b_not_registered, Error.similarity_song_a_not_registered]
        self.assert_correct_print(self.program.do_similar, inputs, expected_messages)

    def test_do_get_song_matches(self):
        inputs = ['', 'A A', 'A', 'A 1', 'B 0', 'B -1', 'A   2', ' ', 'C 3', 'A 1.1']
        expected_messages = [Error.matches_syntax, Error.matches_syntax, Error.matches_syntax, None, None, Error.invalid_num_matches, Error.matches_syntax, Error.matches_syntax, Error.matches_song_not_registered, Error.invalid_num_matches]
        self.assert_correct_print(self.program.do_get_song_matches, inputs, expected_messages)