class Song:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.similar_songs = []

    def add_similar_song(self, song):
        self.similar_songs.append(song)
        song.similar_songs.append(self)
