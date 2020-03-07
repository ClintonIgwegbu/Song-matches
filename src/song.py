from bisect import insort
from bisect import bisect_left

class Song:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.similar_songs = []

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        try:
            return self.name == other.name
        except:
            return False

    # TODO Prevent similar song from being added multiple times
    def add_similar_song(self, song):
        # Insert similar songs into the list, sorted alphabetically.
        if not self._similarity_already_noted(song):
            insort(self.similar_songs, song)
            insort(song.similar_songs, self)
        # self.similar_songs.append(song)
        # song.similar_songs.append(self)

    def _similarity_already_noted(self, x):
        i = bisect_left(self.similar_songs, x)
        if i != len(self.similar_songs) and self.similar_songs[i] == x:
            return True
        else:
            return False