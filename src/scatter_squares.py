import matplotlib.pyplot as plt

# Creates axes object and sets the style for the plot.
plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()

# Scatters a single point (2, 4) on the plot with a size of 200.
# ax.scatter(2, 4, s=200)

# Scatters a series of points defined by the input values and their squares.
x_values = range(1, 1001) # This is the list of inputs; 1 - 1000
y_values = [x ** 2 for x in x_values]  # This is the list of outputs

# Scatter plot with color mapping based on y-values
# c=y_values sets the color of each point based on its y-value.
# cmap=plt.cm.Blues sets the colormap to a blue gradient. Higher y-values will be darker blue.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Set chart title and labels for the axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set the range for each axis
ax.axis([0, 1_100, 0, 1_100_000]) # Set the x-axis from 0 to 1100 and y-axis from 0 to 1,100,000

# The default tick label is scientific notation
ax.ticklabel_format(style='plain', useOffset=False) # Set the tick label format to plain

# Shows the plot with the point.
# plt.show()

# Saves the plot to a file named 'scatter_squares.png' in ../assets directory.
# ../assets/scatter_squares.png tells matplotlib to save the file in the assets directory one level up from src.
# bbox_inches='tight' ensures that the saved figure does not have extra whitespace around it.
plt.savefig('../assets/scatter_squares.png', bbox_inches='tight')