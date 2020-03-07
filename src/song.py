from bisect import insort
from bisect import bisect_left


class Song:
    """A class that encapsulates attributes relevant to a song."""

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.similar_songs = []

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        try:
            return self.name == other.name
        except Exception:
            return False

    def add_similar_song(self, song):
        """Insert similar songs into self.similar_songs, in alphabetical order."""

        if not self._similarity_already_noted(song):
            insort(self.similar_songs, song)
            insort(song.similar_songs, self)

    def _similarity_already_noted(self, song):
        """Return boolean indicating if song has already been inserted in self.similar_songs."""

        i = bisect_left(self.similar_songs, song)
        if i != len(self.similar_songs) and self.similar_songs[i] == song:
            return True
        else:
            return False
