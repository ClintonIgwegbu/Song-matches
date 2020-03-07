import unittest
from match_service import MatchService
from song import Song


class TestMatchService(unittest.TestCase):

    def reset_test_dfs(self, song):
        """Reset list of top rated songs and record of visited nodes
        before each call to MatchService._dfs_similarity_graph."""

        num_top_rated_similar_songs = 1
        top_rated_songs = [0] * num_top_rated_similar_songs
        visited = {}
        visited[song.name] = True
        return num_top_rated_similar_songs, top_rated_songs, visited

    def assert_visited(self, conditions, songs, visited):
        """Make assertions on which nodes in similarity graph have been visited."""

        for i in range(6):
            with self.subTest():
                if conditions[i] is True:
                    self.assertTrue(songs[i].name in visited)
                else:
                    self.assertFalse(songs[i].name in visited)

    def setup_songs(self, a, b, c, d, e, f, g):
        """Initialise seven songs."""

        return Song('a', a), Song('b', b), Song('c', c), Song('d', d), Song('e', e), Song('f', f), Song('g', g)

    def test_dfs_similarity_graph(self):
        # Grouped components of graph are {a,b,c,d}; {e,f}
        song_a, song_b, song_c, song_d, song_e, song_f, _ = self.setup_songs(
            1.1, 3.3, 2.5, 4.7, 5.7, 3.6, 0)
        song_a.add_similar_song(song_b)
        song_a.add_similar_song(song_c)
        song_b.add_similar_song(song_d)
        song_c.add_similar_song(song_d)
        song_e.add_similar_song(song_f)
        songs = [song_a, song_b, song_c, song_d, song_e, song_f]

        # Check which nodes can be visited, starting from song_a.
        num_top_rated_similar_songs, top_rated_songs, visited = self.reset_test_dfs(song_a)
        MatchService._dfs_similarity_graph(
            song_a, top_rated_songs, num_top_rated_similar_songs, visited)
        self.assert_visited([True, True, True, True, False, False], songs, visited)

        # Check which nodes can be visited, starting from song_e.
        num_top_rated_similar_songs, top_rated_songs, visited = self.reset_test_dfs(song_e)
        MatchService._dfs_similarity_graph(
            song_e, top_rated_songs, num_top_rated_similar_songs, visited)
        self.assert_visited([False, False, False, False, True, True], songs, visited)

        # Grouped components of graph are now {a,b,c,d,e,f}.
        # Check which nodes can be visited, starting from song_e.
        song_f.add_similar_song(song_b)
        num_top_rated_similar_songs, top_rated_songs, visited = self.reset_test_dfs(song_e)
        MatchService._dfs_similarity_graph(
            song_e, top_rated_songs, num_top_rated_similar_songs, visited)
        self.assert_visited([True, True, True, True, True, True], songs, visited)

    def test_update_top_rated(self):
        song_a, song_b, song_c, song_d, song_e, song_f, song_g = self.setup_songs(
            1, 2, 3, 0, 1.1, 2.1, 3.1)
        num_top_rated_similar_songs = 3
        top_rated_songs_before = [song_a, song_b, song_c]

        # Update with song_d
        top_rated_songs_after = top_rated_songs_before[:]
        MatchService._update_top_rated(
            song_d, top_rated_songs_after, num_top_rated_similar_songs)
        with self.subTest():
            self.assertEqual(top_rated_songs_after, [song_a, song_b, song_c])

        # Update with song_e
        top_rated_songs_after = top_rated_songs_before[:]
        MatchService._update_top_rated(
            song_e, top_rated_songs_after, num_top_rated_similar_songs)
        with self.subTest():
            self.assertEqual(top_rated_songs_after, [song_e, song_b, song_c])

        # Update with song_f
        top_rated_songs_after = top_rated_songs_before[:]
        MatchService._update_top_rated(
            song_f, top_rated_songs_after, num_top_rated_similar_songs)
        with self.subTest():
            self.assertEqual(top_rated_songs_after, [song_b, song_f, song_c])

        # Update with song_g
        top_rated_songs_after = top_rated_songs_before[:]
        MatchService._update_top_rated(
            song_g, top_rated_songs_after, num_top_rated_similar_songs)
        with self.subTest():
            self.assertEqual(top_rated_songs_after, [song_b, song_c, song_g])

    def test_shift_and_update(self):
        # Insert at index 0
        top_rated_songs = ['a', 'b', 'c']
        MatchService._shift_and_update('d', top_rated_songs, 0)
        with self.subTest(i=0):
            self.assertEqual(top_rated_songs, ['d', 'b', 'c'])

        # Insert at index 1
        top_rated_songs = ['a', 'b', 'c']
        MatchService._shift_and_update('d', top_rated_songs, 1)
        with self.subTest(i=1):
            self.assertEqual(top_rated_songs, ['b', 'd', 'c'])

        # Insert at index 2
        top_rated_songs = ['a', 'b', 'c']
        MatchService._shift_and_update('d', top_rated_songs, 2)
        with self.subTest(i=2):
            self.assertEqual(top_rated_songs, ['b', 'c', 'd'])

    def test_remove_empty_spaces(self):
        test_values = [0, 4]
        for num_top_rated_similar_songs in test_values:
            top_rated_songs = [0] * num_top_rated_similar_songs
            MatchService._remove_empty_spaces(
                top_rated_songs, num_top_rated_similar_songs)
            with self.subTest(top_rated_songs=top_rated_songs):
                self.assertEqual(top_rated_songs, [])

        top_rated_songs = [0, 0, 'a']
        num_top_rated_similar_songs = len(top_rated_songs)
        MatchService._remove_empty_spaces(
            top_rated_songs, num_top_rated_similar_songs)
        with self.subTest(top_rated_songs=[0, 0, 'a']):
            self.assertEqual(top_rated_songs, ['a'])
