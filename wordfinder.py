"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...

    def __init__(self, path):
        """Read dictionary and reports the number of items read."""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file into a list of words"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random words"""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """WordFinder that deletes blank lines/comments."""
    def parse(self, dict_file):
        """Parse dict_file for the list of words and skip blanks and comments"""
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]