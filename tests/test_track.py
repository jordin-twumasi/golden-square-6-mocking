from lib.track import Track

"""
Given title and artist
and search keyword is full title
matches is true
"""


def test_matches_full_title():
    track = Track('Cat', 'Dog')
    assert track.matches('Cat') == True


"""
Given title and artist
and search keyword is full artist
matches is true
"""


def test_matches_full_artist():
    track = Track('Cat', 'Dog')
    assert track.matches('Dog') == True
    
    
"""
Given title and artist
and search keyword is partial title
matches is true
"""


def test_matches_partial_title():
    track = Track('Cat in Hat', 'Dog')
    assert track.matches('Cat') == True


"""
Given title and artist
and search keyword is partial artist
matches is true
"""


def test_matches_full_title():
    track = Track('Cat', 'Dog in Hat')
    assert track.matches('Dog') == True


"""
Given title and artist
and search keyword is neither title nor artist
matches is false
"""


def test_matches_full_title():
    track = Track('Cat', 'Dog')
    assert track.matches('Mouse') == False
    