class Error:
    """Error messages for invalid user input."""

    invalid_command = ("\nCommand not recognised.\n"
                       "Enter '?' or 'help' for more information.\n")

    song_syntax = ("\nYou have not entered the command in the correct format.\n"
                   "Register a song using the format: song song_name rating\n"
                   "Enter '?' or 'help' for more information.\n")

    invalid_rating = ("\nRating must be a number.\n")

    similarity_syntax = ("\nYou have not entered the command in the correct format.\n"
                         "Register song similarities using the format: similar song_a song_b\n"
                         "Enter '?' or 'help' for more information.\n")

    same_song = ("\nYou entered the same song twice. Enter two different songs.\n")

    neither_song_registered = ("\nNeither song has been registered yet.\n"
                               "Register a song using the format: song song_name rating\n"
                               "Enter '?' or 'help' for more information.\n")

    song_a_not_registered = ("\nThe first song has not been registered yet.\n"
                             "Register a song using the format: song song_name rating\n"
                             "Enter '?' or 'help' for more information.\n")

    song_b_not_registered = ("\nThe second song has not been registered yet.\n"
                             "Register a song using the format: song song_name rating\n"
                             "Enter '?' or 'help' for more information.\n")

    matches_syntax = ("\nYou have not entered the command in the correct format.\n"
                      "Get song matches using the format: get_song_matches song_name num_matches\n"
                      "Enter '?' or 'help' for more information.\n")

    invalid_num_matches = ("Invalid number of matches.")

    matches_song_not_registered = ("\nThat song has not been registered yet.\n"
                                   "Register a song using the format: song song_name rating\n"
                                   "Enter '?' or 'help' for more information.\n")

    song_already_registered = ("\nYou have already registered that song.\n"
                               "Enter '?' or 'help' for more information.\n")

    remove_similar_syntax = ("\nYou have not entered the command in the correct format.\n"
                             "Remove song similarities using the format: remove_similar song_a song_b\n"
                             "Enter '?' or 'help' for more information.\n")


class Notice:
    """Notifications for the user."""

    confirm_delete_all_sim = ("\nAre you sure you would like to delete all similarities? (Y/N)")

    @staticmethod
    def rating_updated(name, rating):
        return ("\n{0}'s rating is now {1}.\n".format(name, rating))
