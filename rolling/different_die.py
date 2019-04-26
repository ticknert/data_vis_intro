# A program for rolling two dice.

from die import Die
import pygal

# Create two different dice.
die_1 = Die(6)
die_2 = Die(10)

# Roll some times and store it in a list.
results = []
rolls = input("How many times would you like to roll the die? ")
for roll in range(1, int(rolls)+1):
    results.append(die_1.roll_die() + die_2.roll_die())

# Analyze the results.
frequencies = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D" + str(die_1.sides) + " and a D"
hist.title += str(die_2.sides) + " die " + rolls + " times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16']
hist.y_title = "Result"
hist.x_title = "Frequency of Result"

hist.add('D'+str(die_1.sides)+' + D'+str(die_2.sides), frequencies)
hist.render_to_file('visuals/more_visual.svg')