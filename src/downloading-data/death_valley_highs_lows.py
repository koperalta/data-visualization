from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Read the CSV file
path = Path("src/downloading-data/weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)

# Read the header row
header_row = next(reader)

# Print the index and header names
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Convert remaining rows to a list for multiple passes
dates, highs, lows = [], [], []

for row in reader :
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try :
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else :
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5) # Plot high temperatures in red
ax.plot(dates, lows, c='blue', alpha=0.5) # Plot low temperatures in blue

ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Fill the area between high and low temperatures

# Format the plot
ax.set_title("Daily high & low temperatures - 2021\n ", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Display the plot
plt.show()