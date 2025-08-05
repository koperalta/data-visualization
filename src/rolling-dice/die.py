from random import randint

class Die :
    """ A class representing a single die. """
    
    def __init__(self, sides=6):
        """ Assumes a six-sided die by default. """
        self.num_sides = sides
    
    def roll(self) :
        """ Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)