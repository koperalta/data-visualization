import matplotlib.pyplot as plt

# Creates axes object and sets the style for the plot.
plt.style.use("seaborn-v0_8-dark-palette")
fig, ax = plt.subplots()

# Creates dataset of x-values and y-values.
x_values = range(1, 5001)  # This is the list of inputs; 1 to 5000
y_values = [x ** 3 for x in x_values]  # This is the list of outputs

# Scatter plot with the given dataset
# c=y_values sets the color of each point based on its y-value.
# cmap=plt.cm.Blues sets the colormap to a blue gradient. Higher y-values will be darker blue.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)

# Set chart title and labels for the axes.
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set the range for each axis
ax.axis([0, 5000, 0, 125000000000])  # Set the x-axis from 0 to 5000 and y-axis from 0 to the maximum cube value

# Show the plot
# plt.show()

# Save the plot in the assets directory
# Saves the plot to a file named 'scatter_cubes.png' in the assets directory
# bbox_inches='tight' ensures that the saved figure does not have extra whitespace around it.
plt.savefig('assets/scatter_cubes.png', bbox_inches='tight')