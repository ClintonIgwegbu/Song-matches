class MatchService:

    # Clinton included song_dict as a parameter
    @staticmethod
    def get_song_matches(song, num_top_rated_similar_songs, song_dict):
        """
        :param song: Current Song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        :return: List of top rated similar songs
        """

        # No similar songs
        if num_top_rated_similar_songs == 0:
            return []

        s = song_dict[song]
        visited = {}  # Create a dictionary of visited nodes and add song s to it
        visited[s.name] = True  # Dictionary is used because of its contant time access

        top_rated_songs = [0]*num_top_rated_similar_songs
        # traverse graph starting from song
        MatchService.dfs_similarity_graph(s, top_rated_songs, num_top_rated_similar_songs, song_dict, visited)
        MatchService.remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs)

        return top_rated_songs

    # TODO Consider putting some of below methods in another file e.g. perhaps dfs under song?
    # TODO How to indicate that top_rated_songs is updated in some of the functions below?
    @staticmethod
    def dfs_similarity_graph(song, top_rated_songs, num_top_rated_similar_songs, song_dict, visited):
        """
        :param song: Current song
        :param top_rated_songs: List of the top rated songs that are similar to song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        :param song_dict: Dictionary of songs the user has entered; key is song name, value is Song object
        :visited: Dictionary of 'visited' nodes in the graph traversal
        """
        for s in song.similar_songs:
            if s.name not in visited:
                visited[s.name] = True
                MatchService.update_top_rated(s, top_rated_songs, num_top_rated_similar_songs, song_dict)
                MatchService.dfs_similarity_graph(s, top_rated_songs, num_top_rated_similar_songs, song_dict, visited)

    @staticmethod
    def update_top_rated(song, top_rated_songs, num_top_rated_similar_songs, song_dict):
        """
        :param song: Current song
        :param top_rated_songs: List of the top rated songs that are similar to song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        :param song_dict: Dictionary of songs the user has entered; key is song name, value is Song object
        """
        for i in range(num_top_rated_similar_songs - 1, -1, -1):
            if top_rated_songs[i] == 0:
                MatchService.shift_and_update(song, top_rated_songs, i)
                break
            elif song.rating > top_rated_songs[i].rating:
                MatchService.shift_and_update(song, top_rated_songs, i)
                break

    @staticmethod
    def shift_and_update(song, top_rated_songs, index):
        """
        :param song: Current song
        :param top_rated_songs: List of the top rated songs that are similar to song
        :param index: Index where song should replace value in top_rated_songs
        """
        for i in range(index + 1):
            if i == index:
                top_rated_songs[i] = song
            else:
                top_rated_songs[i] = top_rated_songs[i+1]

    @staticmethod
    def remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs):
        """
        :param top_rated_songs: List of the top rated songs that are similar to song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        """
        if top_rated_songs == []:
            return

        while top_rated_songs[0] == 0:
            top_rated_songs.pop(0)
            if top_rated_songs == []:
                return
