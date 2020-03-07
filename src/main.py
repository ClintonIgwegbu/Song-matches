# TODO: Currently an attempt to edit a song rating breaks the whole program. Fix this
# There must be a way to remove/update similar songs for each song that references a changed song
# Or perhaps create a new method in main called update, use to update song ratings such that repeated calls to song command
# don't do anything and tell the user that they already registered the song - to update the rating do this
# TODO: Perhaps another method to remove a song completely from the graph
# TODO: Perhaps another method to reset i.e. erase all similarities
# TODO: Perhaps another method to remove specific similarities
# TODO: We must undergeez to get a place on this internship! Think of further extensions
# TODO: Perhaps move some of the error-catching here to the functions being called?

from cmd import Cmd
from song import Song
from match_service import MatchService
from error_messages import Error


class Program(Cmd):

    song_dict = {}  # Record of songs registered by the user

    def do_exit(self, inp):
        """Exit the program."""

        print("Bye")
        return True

    def do_song(self, inp):
        """
        Allows user to register a song into the 'database'.

        Song is registered using format: song song_name rating
        """

        try:
            (name, rating) = inp.split(" ")
        except Exception:
            print(Error.song_syntax)
            return

        # TODO: Either allow song ratings to be changed or don't and forget about extensions
        try:
            song_already_seen = name in self.song_dict
            if song_already_seen:
                # self.song_dict[name].rating = rating
                print(Error.song_already_registered)
            else:
                self.song_dict[name] = Song(name, float(rating))

        except Exception:
            if rating != '':
                print(Error.invalid_rating)
            else:
                print(Error.song_syntax)

    def do_similar(self, inp):
        """
        Allows user to register similarities between songs in the 'database'.

        Register similarity using format: similarity song_a_name song_b_name
        """

        try:
            (song_a, song_b) = inp.split(" ")
        except Exception:
            print(Error.similarity_syntax)
            return

        if song_a in self.song_dict and song_b in self.song_dict and song_a != song_b:
            self.song_dict[song_a].add_similar_song(
                self.song_dict[song_b])  # Valid input
        elif song_a == '':
            print(Error.similarity_syntax)
        elif song_a == song_b:
            print(Error.same_song)
        elif song_a not in self.song_dict and song_b not in self.song_dict:
            print(Error.similarity_neither_song_registered)
        elif song_a not in self.song_dict:
            print(Error.similarity_song_a_not_registered)
        elif song_b not in self.song_dict:
            print(Error.similarity_song_b_not_registered)

    def do_get_song_matches(self, inp):
        """
        Allows user to get the highest rated songs similar to any song in the database.

        Use format: get_song_matches song_name num_top_rated_similar_songs
        """

        try:
            (name, num_top_rated_similar_songs) = inp.split(" ")
        except Exception:
            print(Error.matches_syntax)
            return

        try:
            if not float(num_top_rated_similar_songs).is_integer():
                print(Error.invalid_num_matches)
            elif int(num_top_rated_similar_songs) < 0:
                print(Error.invalid_num_matches)
            elif name not in self.song_dict:
                print(Error.matches_song_not_registered)
            else:
                # Valid input
                matches = MatchService.get_song_matches(
                    self.song_dict[name], int(num_top_rated_similar_songs))
                self._print_results(matches)
        except Exception:
            print(Error.matches_syntax)

    # def do_edit_rating(self, inp):
    #     """Edit the rating of a song."""

    #     (name, rating) = inp.split(" ")
    #     self.song_dict[name] = Song(name, float(rating))
    #     update_similarity_graph()

    # def do_remove_song(self, inp):
    #     """Remove a song from the 'database'."""
    #     name = inp.split(" ")
    #     self.song_dict[name].remove_from_other_songs_similarity()
    #     del self.song_dict[name]

    # def do_remove_similarity(self, inp):
    #     """Delete record of similarity between two songs."""
    #     (song_a, song_b) = inp.split(" ")
    #     self.song_dict[song_a].remove_song_similarity(song_b)

    # def do_reset_similarity(self, inp):
    #     """Delete records of all similarities."""
    #     for name in self.song_dict:
    #         self.song_dict[name].remove_all_similarities()

    def _print_results(self, result):
        """Print the results of do_get_song_matches to the console."""

        output = "result "
        output += "<null>" if not result else " ".join(
            [song.name for song in sorted(result, key=lambda x: x.name)]
        )
        print(output)


if __name__ == "__main__":
    Program().cmdloop()
