from lib.music_library import MusicLibrary
from lib.track import Track


"""Adding multiple track, adds to list"""
def test_search_by_title_or_artist():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1]


"""
When we add two tracks
And we search for a word in the title or artist
We get the matching track back
"""
def test_search_by_title_or_artist():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Way") == [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title or artist
We get the matching track back
"""
def test_search_by_part_of_title_or_artist():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search("lace") == [track_2]


"""
When we add two tracks
And we search for a word not in any track title or artist
We get an empty list back
"""

def test_search_by_word_not_in_title_or_artist_returns_empty():

    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search("zzz") == []


