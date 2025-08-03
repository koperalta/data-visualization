import matplotlib.pyplot as plt

# Creates axes object and sets the style for the plot.
plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()

# Scatters a single point (2, 4) on the plot with a size of 200.
ax.scatter(2, 4, s=200)

# Shows the plot with the point.
plt.show()