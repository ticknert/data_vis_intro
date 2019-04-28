# Create a random walk class for how our 'ant' will make decisions

from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """
    A class to generate random walks.\n
    Methods:\n
    \tfill_walk() > Generate plot points with number of steps\n
    \tplot_walk() > Plot the walk, args are start_finish and remove_axes
    """

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

    def plot_walk(self, start_finish=False, remove_axes=False):
        """
        Generate a plot of the walk.\n
        start_finish = T/F --> big green and red dots at beginning and end.\n
        remove_axis = T/F --> self explanatory
        """
        numpoints = list(range(self.steps))

        # Give the plot a colormap to show beginning and end.
        plt.scatter(self.x_value, self.y_value, c=numpoints, cmap=plt.cm.Blues, 
            edgecolor='none', s=10)

        # If we want to emphasize the first and last points, do this.
        if start_finish:
            plt.scatter(self.x_value[0], self.y_value[0], c='green', edgecolors='none', 
                s=100)
            plt.scatter(self.x_value[-1], self.y_value[-1], c='red', edgecolors='none', 
                s=100)
        
        # If we want to remove the axis, we can do it like this.
        if remove_axes:
            plt.axes().get_xaxis().set_visible(False)
            plt.axes().get_yaxis().set_visible(True)

        # Set the size of the plotting window.
        plt.figure(dpi=128, figsize=(10, 6))

        # Show the plot
        plt.show()