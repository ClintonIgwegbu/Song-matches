class Error:
    """Error messages for invalid user input."""

    song_syntax = ("You have not entered the command in the correct format.\n"
                   "Register a song using the format: song song_name rating")

    invalid_rating = ("Rating must be a number.")

    similarity_syntax = ("You have not entered the command in the correct format.\n"
                         "Register song similarities using the format: similar song_a song_b")

    same_song = ("You entered the same song twice. Enter two different songs.")

    similarity_neither_song_registered = ("Neither song has been registered yet.\n"
                                          "Register a song using the format: song song_name rating")

    similarity_song_a_not_registered = ("The first song has not been registered yet.\n"
                                        "Register a song using the format: song song_name rating")

    similarity_song_b_not_registered = ("The second song has not been registered yet.\n"
                                        "Register a song using the format: song song_name rating")

    matches_syntax = ("You have not entered the command in the correct format.\n"
                      "Get song matches using the format: get_song_matches song_name num_matches")

    invalid_num_matches = ("Invalid number of matches.")

    matches_song_not_registered = ("That song has not been registered yet.\n"
                                   "Register a song using the format: song song_name rating")
