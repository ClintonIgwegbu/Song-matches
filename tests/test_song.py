import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        """Initialise four songs before each test."""

        self.song_a = Song('a', 1)
        self.song_b = Song('b', 2)
        self.song_c = Song('c', 3)
        self.song_d = Song('d', 4)

    def test_find_song(self):
        self.song_a.similar_songs.append(self.song_b)
        self.song_a.similar_songs.append(self.song_c)
        self.assertNotEqual(self.song_a._find_song(self.song_b), -1)
        self.assertNotEqual(self.song_a._find_song(self.song_c), -1)
        self.assertEqual(self.song_a._find_song(self.song_d), -1)

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
