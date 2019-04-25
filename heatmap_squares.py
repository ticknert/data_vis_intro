# Use a scatter plot to generate a heatmap.

from matplotlib import pyplot as plt

# Let's create a lot of values using loops
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# Give custom characteristics for the plot using other arguments
# Colors can be RGB color model or strings
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolors='none', s=15)

# Set plot title and label axis.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize=18)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=10)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# We can save the plot if we would like.
# plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()