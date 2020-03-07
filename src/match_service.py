class MatchService:
    """A utility for returning the highest rated songs that are similar to a specified song."""

    @staticmethod
    def get_song_matches(song, num_top_rated_similar_songs):
        """
        Get highest rated songs that are similar to a given song.

        :param song: Current Song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        :return top_rated_songs: List of top rated similar songs
        """

        if num_top_rated_similar_songs == 0:
            return []

        visited = {}  # Dictionary of visited nodes for depth-firstt traversal of similarity graph
        visited[song.name] = True

        # Fetch list of top rated songs
        top_rated_songs = [0]*num_top_rated_similar_songs
        MatchService._dfs_similarity_graph(song, top_rated_songs, num_top_rated_similar_songs, visited)
        MatchService._remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs)

        return top_rated_songs

    @staticmethod
    def _dfs_similarity_graph(song, top_rated_songs, num_top_rated_similar_songs, visited):
        """
        Perform a depth-first traversal of similarity graph, while updating list of top rated songs
        and dictionary of visited nodes.

        :param song: Current Song
        :param top_rated_songs: List of the top rated songs that are similar to song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        :param visited: Dictionary of 'visited' nodes in the graph traversal
        """
        for similar_song in song.similar_songs:
            if similar_song.name not in visited:
                visited[similar_song.name] = True
                MatchService._update_top_rated(similar_song, top_rated_songs, num_top_rated_similar_songs)
                MatchService._dfs_similarity_graph(similar_song, top_rated_songs, num_top_rated_similar_songs, visited)

    @staticmethod
    def _update_top_rated(song, top_rated_songs, num_top_rated_similar_songs):
        """
        Update list of top rated songs given param song.

        :param song: Current song
        :param top_rated_songs: List of the top rated songs that are similar to song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        """
        for i in range(num_top_rated_similar_songs - 1, -1, -1):
            if top_rated_songs[i] == 0:
                MatchService._shift_and_update(song, top_rated_songs, i)
                break
            elif song.rating > top_rated_songs[i].rating:
                MatchService._shift_and_update(song, top_rated_songs, i)
                break

    @staticmethod
    def _shift_and_update(song, top_rated_songs, index):
        """
        Update rank of songs currently in list of top rated songs, and insert new song in appropriate rank.

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
    def _remove_empty_spaces(top_rated_songs, num_top_rated_similar_songs):
        """
        If allowance made in list of top rated songs is too large, remove empty slots.

        :param top_rated_songs: List of the top rated songs that are similar to song
        :param num_top_rated_similar_songs: the maximum number of song matches to return
        """
        if top_rated_songs == []:
            return

        while top_rated_songs[0] == 0:
            top_rated_songs.pop(0)
            if top_rated_songs == []:
                return
