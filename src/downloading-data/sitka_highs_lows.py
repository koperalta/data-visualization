from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Read the CSV file
path = Path("src/downloading-data/weather_data/sitka_weather_2021_simple.csv")

# Store a list of lines from the CSV file and store it in a variable
lines = path.read_text().splitlines()

# Create a CSV reader object
reader = csv.reader(lines)

# Read the header row
header_row = next(reader)

# Print the index and header names
# enumerate(header_row) returns a list of tuples, where each tuple contains the index and the corresponding header name
# index represents the first element of the tuple, and column_header represents the second element
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Convert remaining rows to a list for multiple passes
# Each element in rows is a list representing a row in the CSV file, where each list contains the values of that row
rows = list(reader)

# Use list comprehensions to extract dates, highs, and lows
dates = [datetime.strptime(row[2], "%Y-%m-%d") for row in rows]
highs = [int(row[4]) for row in rows]
lows = [int(row[5]) for row in rows]

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8') # Use seaborn style for the plot
fig, ax = plt.subplots() # Create a figure and axis for the plot

ax.plot(dates, highs, c='red', alpha=0.5) # Plot high temperatures in red
ax.plot(dates, lows, c='blue', alpha=0.5) # Plot low temperatures in blue

ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Fill the area between high and low temperatures

# Format the plot
ax.set_title("Daily high & low temperatures - 2021", fontsize=24) # Set the title of the plot
ax.set_xlabel("", fontsize=16) # Set the x-axis label
fig.autofmt_xdate() # Automatically format the x-axis dates for better readability
ax.set_ylabel("Temperature (F)", fontsize=16) # Set the y-axis label
ax.tick_params(labelsize=16) # Set the tick parameters for both axes

plt.show()