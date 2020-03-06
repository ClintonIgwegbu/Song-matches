import unittest
from match_service import MatchService

class TestMain(unittest.TestCase):
    # These methods take input from the user, so definitely do need to be tested

    # TODO for these functions, put multiple different input test cases in a file just as you tested in the terminal
    def test_do_song(inp):

    def test_do_similar(inp):

    def test_do_get_song_matches(inp):

class TestMatchService(unittest.TestCase):

    def test_one_should_equal_one(self):
        self.assertEqual(1, 1)

    # TODO How to take graph from input file?
    # def test_dfs_similarity_graph():

    # def test_update_top_rated():

    # def test_shift_and_update():

    # TODO How to setup/teardown test methods and change a test case variable rather than repeating code?
    def test_remove_empty_spaces(self):
        num_top_rated_similar_songs = 0
        top_rated_songs = [0] * num_top_rated_similar_songs
        try:
            remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs)
        assert num_top_rated_similar_songs == []

        num_top_rated_similar_songs = 4
        top_rated_songs = [0] * num_top_rated_similar_songs
        try:
            remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs)
        assert num_top_rated_similar_songs == []

