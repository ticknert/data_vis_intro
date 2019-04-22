# Use a scatter plot instead of a line to plot square numbers again.

from matplotlib import pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values, y_values, s=100)

# Set plot title and label axis.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize=18)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()