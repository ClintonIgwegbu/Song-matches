import unittest
# TODO: Should I import this class or is there a better way to include function definitions?
from src.match_service import MatchService
from src.song import Song

# class TestMain(unittest.TestCase):
    # These methods take input from the user, so definitely do need to be tested

    # TODO for these functions, put multiple different input test cases in a file just as you tested in the terminal
    # def test_do_song(inp):

    # def test_do_similar(inp):

    # def test_do_get_song_matches(inp):

class TestSong(unittest.TestCase):

    def test_add_similar_song(self):
        song_a = Song('a', 1)
        song_b = Song('b', 2)
        song_c = Song('b', 3)
        with self.subTest():
            song_a.add_similar_song(song_b)
            self.assertEqual(len(song_a.similar_songs), 1)
        with self.subTest():
            song_a.add_similar_song(song_b)
            self.assertEqual(len(song_a.similar_songs), 1)  # Same song should not be added to graph twice
        with self.subTest():
            song_a.add_similar_song(song_c)
            self.assertEqual(len(song_a.similar_songs), 2)


class TestMatchService(unittest.TestCase):

    def test_one_should_equal_one(self):
        self.assertEqual(1, 1)

    # TODO Does this really have to be tested? It seems pretty high leve.
    # def test_get_song_matches():


    # TODO How to take graph from input file?
    def test_dfs_similarity_graph(self):
        # In below setup the grouped components of graph are {A,B,C,D}; {E,F}
        song_dict = {}
        song_dict['A'] = Song('A', 1.1)
        song_dict['B'] = Song('B', 3.3)
        song_dict['C'] = Song('C', 2.5)
        song_dict['D'] = Song('D', 4.7)
        song_dict['E'] = Song('D', 5.7)
        song_dict['F'] = Song('D', 3.6)
        song_dict['A'].add_similar_song(song_dict['B'])
        song_dict['A'].add_similar_song(song_dict['C'])
        song_dict['B'].add_similar_song(song_dict['D'])
        song_dict['C'].add_similar_song(song_dict['D'])
        song_dict['E'].add_similar_song(song_dict['F'])

        # TODO: Perhaps the white lines below could be called in separately or put in some kind of setup
        # Check which nodes can be visited, starting from 'A'.
        num_top_rated_similar_songs = 1
        top_rated_songs = [0] * num_top_rated_similar_songs
        visited = {}
        visited['A'] = True
        MatchService.dfs_similarity_graph(song_dict['A'], top_rated_songs, num_top_rated_similar_songs, song_dict, visited)
        with self.subTest(song='A'):
            self.assertTrue('A' in visited)
        with self.subTest(song='B'):
            self.assertTrue('B' in visited)
        with self.subTest(song='C'):
            self.assertTrue('C' in visited)
        with self.subTest(song='D'):
            self.assertTrue('D' in visited)
        with self.subTest(song='E'):
            self.assertFalse('E' in visited)
        with self.subTest(song='F'):
            self.assertFalse('F' in visited)

        # Check which nodes can be visited, starting from 'E'
        num_top_rated_similar_songs = 1
        top_rated_songs = [0] * num_top_rated_similar_songs
        visited = {}
        visited['E'] = True
        MatchService.dfs_similarity_graph(song_dict['E'], top_rated_songs, num_top_rated_similar_songs, song_dict, visited)
        with self.subTest(song='A'):
            self.assertFalse('A' in visited)
        with self.subTest(song='B'):
            self.assertFalse('B' in visited)
        with self.subTest(song='C'):
            self.assertFalse('C' in visited)
        with self.subTest(song='D'):
            self.assertFalse('D' in visited)
        with self.subTest(song='E'):
            self.assertTrue('E' in visited)
        with self.subTest(song='F'):
            self.assertTrue('F' in visited)

        # In below setup the gouped components of graph are {A,B,C,D,E,F};
        # Check which nodes can be visited, starting from 'E'
        song_dict['F'].add_similar_song(song_dict['B'])
        num_top_rated_similar_songs = 1
        top_rated_songs = [0] * num_top_rated_similar_songs
        visited = {}
        visited['E'] = True
        MatchService.dfs_similarity_graph(song_dict['E'], top_rated_songs, num_top_rated_similar_songs, song_dict, visited)
        with self.subTest(song='A'):
            self.assertTrue('A' in visited)
        with self.subTest(song='B'):
            self.assertTrue('B' in visited)
        with self.subTest(song='C'):
            self.assertTrue('C' in visited)
        with self.subTest(song='D'):
            self.assertTrue('D' in visited)
        with self.subTest(song='E'):
            self.assertTrue('E' in visited)
        with self.subTest(song='F'):
            self.assertTrue('F' in visited)

    # TODO
    # def test_update_top_rated():

    def test_shift_and_update(self):
        top_rated_songs = ['a', 'b', 'c']
        MatchService.shift_and_update('d', top_rated_songs, 0)
        with self.subTest(i=0):
            self.assertEqual(top_rated_songs, ['d', 'b', 'c'])

        top_rated_songs = ['a', 'b', 'c']
        MatchService.shift_and_update('d', top_rated_songs, 1)
        with self.subTest(i=1):
            self.assertEqual(top_rated_songs, ['b', 'd', 'c'])

        top_rated_songs = ['a', 'b', 'c']
        MatchService.shift_and_update('d', top_rated_songs, 2)
        with self.subTest(i=2):
            self.assertEqual(top_rated_songs, ['b', 'c', 'd'])

    # TODO How to setup/teardown test methods and change a test case variable rather than repeating code?
    def test_remove_empty_spaces(self):
        # NOTE: Input functions should not allow negative test values to get through
        test_values = [0, 4]
        for num_top_rated_similar_songs in test_values:
            top_rated_songs = [0] * num_top_rated_similar_songs
            MatchService.remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs)
            with self.subTest(num_top_rated_similar_songs = num_top_rated_similar_songs):
                self.assertEqual(top_rated_songs, [])

        top_rated_songs = [0, 0, 'a']
        num_top_rated_similar_songs = len(top_rated_songs)
        MatchService.remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs)
        with self.subTest(top_rated_songs = [0, 0, 'a']):
            self.assertEqual(top_rated_songs, ['a'])

