from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Read the CSV file
path = Path("src/downloading-data/weather_data/sitka_weather_2021_simple.csv")

# Stores a list of lines from the CSV file and store it in a variable
lines = path.read_text().splitlines()

# Create a CSV reader object with the lines, used to iterate over the rows
reader = csv.reader(lines)

# Read the header row
header_row = next(reader)

# Print the index and header names
# enumerate(header_row) returns a list of tuples, where each tuple contains the index and the corresponding header name
# index represents the first element of the tuple, and column_header represents the second element
for index, column_header in enumerate(header_row) :
    print(index, column_header)

# Extract date and high temperatures from the CSV file
dates, highs = [], []
for row in reader :
    # Convert the high temperature from string to integer and append it to the highs list
    highs.append(int(row[4]))
    dates.append(datetime.strptime(row[2], "%Y-%m-%d"))  # Append the date to the dates list

# Plot the high temperatures
plt.style.use('seaborn-v0_8') # Use seaborn style for the plot
fig, ax = plt.subplots() # Create a figure and axis for the plot

# Plot the high temperatures against the dates, with red color
# The method ax.plot() knows which to put on the x-axis and which on the y-axis based on the order of the arguments
# The first argument is the x-axis data (dates) and the second argument is the y-axis data (highs)
# If it just highs, it would plot the highs against their index in the list
# If only highs were provided, it would plot the highs against their index in the list.
# Ensure that dates and highs are of the same length to avoid errors.
ax.plot(dates, highs, c='red')

# Format the plot
ax.set_title("Daily high temperatures - 2021", fontsize=24) # Set the title of the plot
ax.set_xlabel("", fontsize=16) # Set the x-axis label
fig.autofmt_xdate() # Automatically format the x-axis dates for better readability
ax.set_ylabel("Temperature (F)", fontsize=16) # Set the y-axis label


# Set the tick parameters for both axes
# tick parameters control the appearance of the ticks on the axes
# ticks are the small lines that mark the values on the axes
ax.tick_params(labelsize=16) # Set the tick parameters for both axes

# Display the plot
plt.show()
