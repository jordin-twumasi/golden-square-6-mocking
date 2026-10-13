from lib.music_library import MusicLibrary
from unittest.mock import Mock


"""
When I add multiple ttracks and search for keyword 
I get travks matching keyword

"""
def test_search_by_title_or_artist():
    library = MusicLibrary()
    mock_track_matching = Mock()
    mock_track_matching.matches.return_value = True #Focus on what returned
    mock_track_not_match = Mock()
    mock_track_not_match.matches.return_value = False
    library.add(mock_track_matching)
    library.add(mock_track_not_match)
    assert library.search("hello") == [mock_track_matching]


def test_tracks_empty_initially():
    library = MusicLibrary()
    assert library.tracks == []

def test_tracks_added_are_listed():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()
    library.add(track_1)
    library.add(track_2) 
    library.add(track_3)
    assert library.tracks == [track_1, track_2, track_3]