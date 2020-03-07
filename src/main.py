from cmd import Cmd
from song import Song
from match_service import MatchService
from error_messages import Error

# TODO: Add documentation to ALL methods in src and test files
# TODO: The number of try except blocks and if-statements in each method looks kinda messy. Perhaps make it more compact?
class Program(Cmd):

    song_dict = {}

    def do_exit(self, inp):
        print("Bye")
        return True

    def do_song(self, inp):
        try:
            (name, rating) = inp.split(" ")
        except:
            print(Error.song_syntax)
            return

        try:
            self.song_dict[name] = Song(name, float(rating))
        except:
            if rating != '':
                print(Error.invalid_rating)
            else:
                print(Error.song_syntax)

    def do_similar(self, inp):
        try:
            (song_a, song_b) = inp.split(" ")
        except:
            print(Error.similarity_syntax)
            return

        if song_a in self.song_dict and song_b in self.song_dict and song_a != song_b:
            self.song_dict[song_a].add_similar_song(self.song_dict[song_b])
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
        try:
            (name, num_top_rated_similar_songs) = inp.split(" ")
        except:
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
                matches = MatchService.get_song_matches(self.song_dict[name], int(num_top_rated_similar_songs))
                self._print_results(matches)
        except:
            print(Error.matches_syntax)

    def _print_results(self, result):
        output = "result "
        output += "<null>" if not result else " ".join(
            [song.name for song in sorted(result, key=lambda x: x.name)]
        )
        print(output)


if __name__ == "__main__":
    Program().cmdloop()
