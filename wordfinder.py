"""Word Finder: finds random words from a dictionary."""
 import random

class WordFinder:
    """ finds random words from file
    
    >>> wf = WordFinder("basicwords.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
        
    """

    def __init__(self,path):

    """ read file and gives us the number of words read"""

        file = (open(path))

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")

    def parse(self, file):
        """ makes the file into a list of words"""
        return [w.strip() for w in file]

    def random(self):
        """ returns a random word from the list of words"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """subclass of WordFinder that removes commented and blank sections from a file
    >>> swf = SpecialWordFinder("complexwords.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    """
    def parse(self, file):
        """makes a list of words in file and removes blanks and comments"""
        return [w.strip() for w in file 
                if w.strip() and not w.startswith("#")]
