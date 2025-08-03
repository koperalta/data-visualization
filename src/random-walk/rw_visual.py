import matplotlib.pyplot as plt

from random_walk import RandomWalk

# This script generates a random walk and visualizes it using matplotlib.
while True :
    # Create a RandomWalk instance.
    rw = RandomWalk(100_000)

    # Fill the random walk with points.
    rw.fill_walk()

    # Use the classic style for the plot
    plt.style.use('classic')

    # Create a figure and an axes.
    # Set the size of the figure to 15 inches wide and 9 inches tall.
    # dpi=128 sets the resolution of the figure to 128 dots per inch.
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    # range(rw.num_points) returns a range object that represents the numbers from 0 to rw.num_points - 1.
    point_numbers = range(rw.num_points)

    # Scatter plot of the points in the walk with size 1.
    # c=point_numbers assigns a color to each point based on its index in the walk.
    # The colormap plt.cm.Blues is used to create a gradient of blue colors.
    # edgecolors="none" means that the points will not have a border color.
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=1)
    
    # This simulate a pollen grain floating on a pond.
    # ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=1, alpha=0.5)

    # Emphasize the first and last points in the walk by creating another point on top of each.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Start point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # End point
    
    # Removes the axes from the plot.
    ax.get_xaxis().set_visible(False) # Hides the x-axis
    ax.get_yaxis().set_visible(False) # Hides the y-axis

    # Set the aspect ratio of the plot to be equal. Which means that the x and y axes will have the same scale.
    ax.set_aspect('equal')

    # Show the plot
    plt.show()
    
    # Ask the user if they want to generate another random walk.
    keep_running = input("Generate another random walk? (y/n):")
    if keep_running.lower() == 'n':
        break