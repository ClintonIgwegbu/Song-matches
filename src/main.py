import sys
from cmd import Cmd
from song import Song
from match_service import MatchService
from error_messages import Error, Notice

# NOTE: The recursion depth limit of 1000 (default) imposes a constraint on
# the number of similarities between songs. Though this limit still likely
# allows the inclusion of many thousands of songs into the 'similarity graph'.

class Program(Cmd):

    song_dict = {}  # Record of songs registered by the user

    def do_exit(self, inp):
        """Exit the program."""

        print("Bye")
        return True

    def do_song(self, inp):
        """
        Allows song to be registered in the 'database'.

        Song is registered using format: song song_name rating
        Existing song's rating may also be updated using same format.
        """

        try:
            (name, rating) = inp.split(" ")
        except Exception:
            print(Error.song_syntax)
            return

        try:
            song_already_seen = name in self.song_dict
            if song_already_seen:
                self.song_dict[name].rating = float(rating)
                print(Notice.rating_updated(name, rating))
            else:
                self.song_dict[name] = Song(name, float(rating))

        except Exception:
            if rating != '':
                print(Error.invalid_rating)
            else:
                print(Error.song_syntax)

    def do_similar(self, inp):
        """
        Allows similarities between songs to be registered in the 'database'.

        Register similarity using format: similar song_a_name song_b_name
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
            print(Error.neither_song_registered)
        elif song_a not in self.song_dict:
            print(Error.song_a_not_registered)
        elif song_b not in self.song_dict:
            print(Error.song_b_not_registered)

    def do_get_song_matches(self, inp):
        """
        Allows the highest rated songs, similar to any song in the database, to be fetched.

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

    def do_track_entries(self, inp):
        """
        Track registered songs and similarities.

        Show up-to-date entries using format: track_entries
        """

        print()  # Print newline
        for name in self.song_dict:
            print("Title: {0}\nRating: {1}\nSimilar songs:{2}\n".format(
                name, self.song_dict[name].rating,
                [song.name for song in self.song_dict[name].similar_songs]))

    def do_remove_similar(self, inp):
        """
        Allows similarities between songs to be removed from the 'database'.

        Remove similarity using format: remove_similar song_a_name song_b_name
        """

        try:
            (song_a, song_b) = inp.split(" ")
        except Exception:
            print(Error.remove_similar_syntax)
            return
        if song_a in self.song_dict and song_b in self.song_dict and song_a != song_b:
            self.song_dict[song_a].remove_similar_song(
                self.song_dict[song_b])  # Valid input
        elif song_a == '':
            print(Error.remove_similar_syntax)
        elif song_a == song_b:
            print(Error.same_song)
        elif song_a not in self.song_dict and song_b not in self.song_dict:
            print(Error.neither_song_registered)
        elif song_a not in self.song_dict:
            print(Error.song_a_not_registered)
        elif song_b not in self.song_dict:
            print(Error.song_b_not_registered)

    def do_remove_all_similarities(self, inp):
        """
        Deletes similarities between all songs.

        Delete all similarities using the format: remove_similar song_a_name song_b_name
        """

        proceed = self._confirm_response(Notice.confirm_delete_all_sim)

        if not proceed:
            return
        for name in self.song_dict:
            self.song_dict[name].similar_songs = []

    def do_remove_song(self, inp):
        """
        Deletes a song from the record.

        Delete song using format: remove_song song_name
        """

        if inp not in self.song_dict:
            print(Error.remove_song_syntax)
            return

        proceed = self._confirm_response(Notice.confirm_delete_song(inp))
        if not proceed:
            return
        for name in self.song_dict:
            self.song_dict[name].remove_similar_song(self.song_dict[inp])
        del self.song_dict[inp]

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.

        Overrides Cmd.emptyline.
        """
        # Do nothing

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.

        Overrides Cmd.default.

        """
        print(Error.invalid_command)

    def _confirm_response(self, question, default="no"):
        """Ask a yes/no question via input() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

        The "answer" return value is True for "yes" or False for "no".
        """

        valid = {"yes": True, "y": True, "no": False, "n": False}
        if default is None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            sys.stdout.write(question + prompt)
            choice = input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' "
                                 "(or 'y' or 'n').\n")

    def _print_results(self, result):
        """Print the results of do_get_song_matches to the console."""

        output = "result "
        output += "<null>" if not result else " ".join(
            [song.name for song in sorted(result, key=lambda x: x.name)]
        )
        print(output)


if __name__ == "__main__":
    Program().cmdloop()
