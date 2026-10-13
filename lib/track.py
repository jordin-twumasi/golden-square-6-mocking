# File: lib/track.py

class Track:
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title, artist):
        # Parameters:
        #   title: a string
        #   artist: a string
        # Side-effects:
        #   Sets the title and artist properties
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        # Returns:
        # true if keyword matches title or artist
        return keyword in self.title or keyword in self.artist


