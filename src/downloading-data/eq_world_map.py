from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python Object.
path = Path("src/downloading-data/eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text()

# Convert the string to a Python object
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"] # Returns a list of dictionaries.

# Extract specific data from the dictionaries.
magnitudes = [eq["properties"]["mag"] for eq in all_eq_dicts]
longitudes = [eq["geometry"]["coordinates"][0] for eq in all_eq_dicts]
latitudes = [eq["geometry"]["coordinates"][1] for eq in all_eq_dicts]
eq_titles = [eq["properties"]["title"] for eq in all_eq_dicts]

title = "Global Earthquakes"

# Makes the World Map
fig = px.scatter_geo(lon=longitudes, lat=latitudes, size=magnitudes, title=title,
                    color=magnitudes, color_continuous_scale="Viridis",
                    labels={"color": "Magnitude"}, projection="natural earth",
                    hover_name=eq_titles,
                    )
# color=magnitudes tells Python to color the points based on their magnitude.
# color_continuous_scale="Viridis" sets the color scale to Viridis.
# labels={"color": "Magnitude"} sets the label for the color bar.
# projection="natural earth" sets the map projection to a natural Earth view.

fig.show()