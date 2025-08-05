import requests
import json

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")  # Print the status code of the response

# Explore the structure of the data.
response_dict = r.json()  # Convert the response to a JSON object
response_string = json.dumps(response_dict, indent=4)  # Convert the response to a formatted string
print(response_string)  # Print the formatted response string