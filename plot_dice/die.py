# This is a class for rolling a die.

from random import randint

class Die():
    """This is a class representing a single dice."""

    def __init__(self, sides=6):
        """
        Initializes attributes for die class.\n
        Assume a 6-sided die.
        """
        self.sides = sides

    def roll_die(self):
        """Roll the dice. Return random int from 1 to 6."""
        return randint(1,self.sides)