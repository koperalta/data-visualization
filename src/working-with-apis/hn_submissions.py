from operator import itemgetter 

import requests

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"  # URL for top stories on Hacker News
r = requests.get(url)  # Make the GET request to the API
print(f"Status code: {r.status_code}")  # Print the status code of the response

# Process information about each submission
submission_ids = r.json()  # Convert the response to a JSON object

submission_dicts = []  # Initialize an empty list to store submission dictionaries 

# Iterate through the submission IDs and fetch details for each submission
for submission_id in submission_ids[:5]:  # Limit to the first 5 submissions
    # Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"  # URL for a specific submission
    r = requests.get(url)  # Make the GET request to the API
    
    # Print the submission ID and status code
    print(f"id: {submission_id}\tstatus code: {r.status_code}")
    
    # Convert the response to a JSON object and append it to the list
    response_dict = r.json()
    
    # Build a dictionary for each article
    submission_dict = {
        "title": response_dict.get("title", "No title provided"),  # Get the title or default to a placeholder
        "hn_link" : f"https://news.ycombinator.com/item?id={submission_id}",  # Construct the Hacker News link
        "comments": response_dict.get("descendants", 0),  # Get the number of comments or default to 0
    }
    
    # Append the submission dictionary to the list
    submission_dicts.append(submission_dict)

# Sort by number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")  # Print the number of comments