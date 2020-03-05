# README #

### Song Matches ###

All songs are given a score, to represent the quality of their metadata.
We would like to return results to the end user with as high quality metadata as possible.

Songs are also marked as similar to other songs.
This can be represented by what we call a _similarity graph_.

Given a number _**n**_ and a _similarity graph_ of songs, return the _**n**_ highest scoring similar songs for a given song.

* Each given song has a score and a list of similar songs.
* Similarity is commutative i.e. if A is similar to B then B is similar to A.
* Similarity is transitive i.e. if A is similar to B, and B is similar to C, then A is similar to C.
* The order of the songs that are returned does not matter.
* The original song should not be considered in the result.
* If _**n**_ is more than the number of similar songs, then return all of the similar songs.
* If _**n**_ is zero, return no similar songs.


**Example:** Given A, B, C and D songs with the following scores and similarities given as input to our program:
![song-similarities](./song-similarities.jpg)

```
     (Cmd) song A 1.1
     (Cmd) song B 3.3
     (Cmd) song C 2.5
     (Cmd) song D 4.7
     (Cmd) similar A B
     (Cmd) similar A C
     (Cmd) similar B D
     (Cmd) similar C D
```


* get_song_matches(A, 2): should return {B, D}

```
    (Cmd) get_song_matches A 2
    (Cmd) result B D
```


* get_song_matches(A, 4) should return {B, C, D}

```
    (Cmd) get_song_matches A 4
    (Cmd) result B C D
```


* get_song_matches(A, 1) should return D

```
    (Cmd) get_song_matches A 1
    (Cmd) result D
```

Please design a solution that is production ready.

### Running the program

In order to start running the program from the command line please run the following command:

```
$ make run
```

### Running the tests

In order to run all the unit tests from the command line please run the following command:

```
$ make test
```

### System requirements:

- [GNU Make](https://www.gnu.org/software/make/)
- Python3
