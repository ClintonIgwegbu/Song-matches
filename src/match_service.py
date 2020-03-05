class MatchService:

    @staticmethod
    def get_song_matches(song, num_top_rated_similar_songs):
        """
        :param song: Current Song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        :return: List of top rated similar songs
        """
        raise NotImplementedError
