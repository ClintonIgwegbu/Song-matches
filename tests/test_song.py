import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        """Initialise six songs before each test."""

        self.song_a = Song('a', 1)
        self.song_b = Song('b', 2)
        self.song_c = Song('c', 3)
        self.song_d = Song('d', 4)

        self.song_e = Song('e', 5)
        self.song_f = Song('f', 6)
        self.song_e.similar_songs.append(self.song_f)
        self.song_f.similar_songs.append(self.song_e)

    def test_similarity_already_noted(self):
        self.song_a.similar_songs.append(self.song_b)
        self.song_a.similar_songs.append(self.song_c)
        self.assertTrue(self.song_a._similarity_already_noted(self.song_b))
        self.assertTrue(self.song_a._similarity_already_noted(self.song_c))
        self.assertFalse(self.song_a._similarity_already_noted(self.song_d))

    def test_add_similar_song(self):
        with self.subTest('Add song b to graph'):
            self.song_a.add_similar_song(self.song_b)
            self.assertEqual(len(self.song_a.similar_songs), 1)
        with self.subTest('Try to add song b to graph again'):
            self.song_a.add_similar_song(self.song_b)
            # Same song should not be added to graph twice
            self.assertEqual(len(self.song_a.similar_songs), 1)
        with self.subTest('Add song c to graph'):
            self.song_a.add_similar_song(self.song_c)
            self.assertEqual(len(self.song_a.similar_songs), 2)

    def test_remove_similar_song(self):
        with self.subTest("Remove song_f from song_e's similar songs"):
            self.song_e.remove_similar_song(self.song_f)
            self.assertEqual(self.song_e.similar_songs, [])
            self.assertEqual(self.song_f.similar_songs, [])
        with self.subTest("Now try to remove song_f again"):
            self.song_e.remove_similar_song(self.song_f)
            self.assertEqual(self.song_e.similar_songs, [])
            self.assertEqual(self.song_f.similar_songs, [])
