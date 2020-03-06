from cmd import Cmd

from song import Song
from match_service import MatchService

# TODO: The error messages distract from the rest of the file.
# Consider moving them to a separate file?
# Perhaps referenced by enums? or function parameters?
# TODO: Error catching here for bad input
class Program(Cmd):

    song_dict = {}

    def do_exit(self, inp):
        print("Bye")
        return True

    def do_song(self, inp):
        try:
            (name, rating) = inp.split(" ")
        except:
            print("You have not entered the song in the correct format. \
                Enter it using the format: song song_name rating")
            return
        try:
            self.song_dict[name] = Song(name, float(rating))
        except:
            print("The rating must be a number. \
                Note that comma-separation cannot be used.")

    def do_similar(self, inp):
        try:
            (song_a, song_b) = inp.split(" ")
        except:
            print("You have not entered the command in the correct format. \
                Enter it using the format: similar song_a song_b")
            return
        if song_a in self.song_dict and song_b in self.song_dict:
            if song_a == song_b:
                print("You entered the same song twice. Enter two different songs.")
                return
            self.song_dict[song_a].add_similar_song(self.song_dict[song_b])
            return
        if song_a not in self.song_dict and song_b not in self.song_dict:
            print("Neither of those songs have been registered yet. \
                Register a song using the format: song song_name rating")
        elif song_a not in self.song_dict:
            print("The first song has not been registered yet. \
                Register a song using the format: song song_name rating")
        else:
            print("The second song has not been registered yet. \
                Register a song using the format: song song_name rating")

    def do_get_song_matches(self, inp):
        try:
            (song, num_top_rated_similar_songs) = inp.split(" ")
        except:
            print("Your input is not in the correct format. \
                Get song matches using the format: get_song_matches song_name num_matches")
            return
        try:
            if int(num_top_rated_similar_songs) < 0:
                print("You must enter a non-negative number.")
                return
            if song not in self.song_dict:
                print("That has not been registered yet. \
                    Register a song using the format: song song_name rating")
                return
            matches = MatchService.get_song_matches(song, int(num_top_rated_similar_songs), self.song_dict)
            self._print_results(matches)
        except:
            print("The input you entered is incorrect. Try again.")

    def _print_results(self, result):
        output = "result "
        output += "<null>" if not result else " ".join(
            [song.name for song in sorted(result, key=lambda x: x.name)]
        )
        print(output)


if __name__ == "__main__":
    Program().cmdloop()
