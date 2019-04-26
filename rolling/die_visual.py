# Implement the Die class.

from die import Die
import pygal

# Create a six-sided die (also known as a D6).
my_die = Die()

# Make some rolls and store them in a list.
my_rolls = []
rolls = input("How many times would you like to roll the die? ")
for roll in range(1,int(rolls)+1):
    my_rolls.append(my_die.roll_die())

# If we want to analyze the results, we can do this.
frequencies = []
for value in range(1, my_die.sides+1):
    frequency = my_rolls.count(value)
    frequencies.append(frequency)

print(frequencies)

# Make a histogram to visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D" + str(my_die.sides) + ", " 
hist.title += str(rolls) + " times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D'+str(my_die.sides), frequencies)
hist.render_to_file('visuals/die_visual.svg')