from cmd import Cmd

from song import Song
from match_service import MatchService

# TODO: Error catching here for bad input
class Program(Cmd):

    song_dict = {}

    def do_exit(self, inp):
        print("Bye")
        return True

    def do_song(self, inp):
        (name, rating) = inp.split(" ")
        self.song_dict[name] = Song(name, float(rating))

    def do_similar(self, inp):
        (song_a, song_b) = inp.split(" ")
        self.song_dict[song_a].add_similar_song(self.song_dict[song_b])

    def do_get_song_matches(self, inp):
        (song, num_top_rated_similar_songs) = inp.split(" ")

        # TODO: Uncomment the following two lines once your implementation is ready
        matches = MatchService.get_song_matches(song, int(num_top_rated_similar_songs), self.song_dict)
        self._print_results(matches)

    def _print_results(self, result):
        output = "result "
        output += "<null>" if not result else " ".join(
            [song.name for song in sorted(result, key=lambda x: x.name)]
        )
        print(output)


if __name__ == "__main__":
    Program().cmdloop()
