# Use a scatter plot instead of a line to plot square numbers again.

from matplotlib import pyplot as plt

# Let's create a lot of values using loops
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, edgecolors=None, s=15)

# Set plot title and label axis.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize=18)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=10)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()