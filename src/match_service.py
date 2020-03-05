class MatchService:

    # Clinton included song_dict as a parameter
    @staticmethod
    def get_song_matches(song, num_top_rated_similar_songs, song_dict):
        """
        :param song: Current Song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        :return: List of top rated similar songs
        """

        # no similar songs
        if num_top_rated_similar_songs == 0:
            return []

        s = song_dict[song]
        top_rated_songs = [0]*num_top_rated_similar_songs
        # traverse graph starting from song
        MatchService.dfs_similarity_graph(top_rated_songs, s, num_top_rated_similar_songs, song_dict)
        MatchService.remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs)

        return top_rated_songs

    # See if comparison with 0 causes error
    # Consider putting some of below methods in another file e.g. perhaps dfs under song?
    @staticmethod
    def dfs_similarity_graph(top_rated_songs, song, num_top_rated_similar_songs, song_dict):
        for s in song.similar_songs:
            MatchService.update_top_rated(top_rated_songs, s, num_top_rated_similar_songs, song_dict)
            MatchService.dfs_similarity_graph(top_rated_songs, s, num_top_rated_similar_songs, song_dict)

    @staticmethod
    def update_top_rated(top_rated_songs, song, num_top_rated_similar_songs, song_dict):
        for i in range(num_top_rated_similar_songs -  1, -1 , -1):
            if top_rated_songs == 0:
                MatchService.shift_and_update(top_rated_songs, song, i)
                break
            elif song.rating > top_rated_songs[i].rating:
                MatchService.shift_and_update(top_rated_songs, song, i)
                break

    @staticmethod
    def shift_and_update(top_rated_songs, song, index):
        for i in range(index + 1):
            if i == index:
                top_rated_songs[i] = song
            else:
                top_rated_songs[i] = top_rated_songs[i+1]

    @staticmethod
    def remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs):
        for i in range(num_top_rated_similar_songs):
            if top_rated_songs[i] == 0:
                top_rated_songs.pop(0)
            else:
                break
