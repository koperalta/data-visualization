from pathlib import Path
import json

# Read data as a string and convert to a Python Object.
path = Path("src/downloading-data/eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()

# Convert the string to a Python object
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
# path = Path("src/downloading-data/eq_data/readable_eq_data.geojson")
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"] # Returns a list of dictionaries.

# Print the number of earthquakes in the dataset to confirm the data was read correctly.
# print(len(all_eq_dicts))

# Extract specific data from the dictionaries.
magnitudes = [eq["properties"]["mag"] for eq in all_eq_dicts]
longitudes = [eq["geometry"]["coordinates"][0] for eq in all_eq_dicts]
latitudes = [eq["geometry"]["coordinates"][1] for eq in all_eq_dicts]

# Print the first 10 magnitudes, longitudes, and latitudes to confirm extraction.
# print(magnitudes[:10])
# print(longitudes[:10])
# print(latitudes[:10])