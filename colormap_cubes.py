# Tim Tickner
# Exercise 15-1 and 15-2

from matplotlib import pyplot as plt

# Define plot points
x_values = range(1,5001)
y_values = [value**3 for value in x_values]

# Create the plot
plt.scatter(x_values, y_values, s=15, c=x_values, cmap=plt.cm.RdPu, 
    edgecolors='none')

# Give the plot some meaning
plt.title("Plot of first 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")

# Set the tick size on the plot
plt.tick_params(axis='both', which='major', labelsize=12)

# Show the plot
plt.show()