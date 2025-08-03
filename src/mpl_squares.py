import matplotlib.pyplot as plt

# Creates the dataset where the x values are the indices of the list
# and the y values are the squares of those indices.
input_values = [1, 2, 3, 4, 5]  # This is the list of inputs
squares = [1, 4, 9, 16, 25] # This is the list of outputs

# Adds a different style to the plot
plt.style.use('seaborn-v0_8-dark-palette')

# Plotting the dataset using matplotlib
fig, ax = plt.subplots()

# Set the title and labels for the axes with linewidth of 3
ax.plot(input_values, squares, linewidth=3)

# Set chart title and labels axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()