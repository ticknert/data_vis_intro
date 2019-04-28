# Use the RandomWalk class.
from random_walk import RandomWalk

# Keep making random walks as long as the program is active.
print("Enter 'q' to quit at any time.")
while True:
    # Make a walk and plot the points
    steps = input("How many steps would you like to take? ")
    if steps == 'q':
        break
    my_walk = RandomWalk(int(steps))
    my_walk.fill_walk()
    my_walk.plot_walk()