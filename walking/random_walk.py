# Create a random walk class for how our 'ant' will make decisions

from random import choice
from matplotlib import pyplot as plt

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self,steps=5000):
        """Initalize attributes of a walk."""
        self.steps = steps

        # All walks start at (0, 0).
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """Generate the steps using the choice() function."""
        # Keep taking steps until the walk reaches the desired number of points.
        while len(self.x_value) < self.steps:
            # Decide which way to go and how far.
            x_direction = choice([1, -1]) # -1 is left, 1 is right.
            x_distance = choice([0, 1, 2, 3, 4]) # Choose the distance to move.
            x_step = x_direction * x_distance

            y_direction = choice([1, -1]) # -1 is down, 1 is up.
            y_distance = choice([0, 1, 2, 3, 4]) # Choose the distance to move.
            y_step = y_direction * y_distance

            # Calculate the next x and y values.
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            
            # Take the next step
            self.x_value.append(next_x)
            self.y_value.append(next_y)

    def plot_walk(self):
        """Generate a plot of the walk."""
        plt.scatter(self.x_value, self.y_value, s=15)
        plt.show()