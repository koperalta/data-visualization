import requests
import plotly.express as px

# Make an API call and check the response
url = "https://api.github.com/search/repositories" # This URL is for searching repositories on GitHub
url += "?q=language:python+sort:stars+stars:>10000" # Search for Python repositories with more than 10,000 stars

headers = {"Accept" : "application/vnd.github.v3+json"} # Set the headers to accept the GitHub API version 3
r = requests.get(url, headers=headers) # Make the GET request to the API

print(f"Status code: {r.status_code}") # Print the status code of the response

# Convert the response object to a dictionary
response_dict = r.json() # Convert the response to a JSON object

# Process results
print(f"Total repositories: {response_dict['total_count']}") # Print the total number of repositories found
print(f"Completed results: {not response_dict['incomplete_results']}") # Check if the results are complete

# Process repository information
repo_dicts = response_dict['items'] # Get the list of repositories from the response

# Prepares repository name, stars and URLs for the visualization
repo_names = [repo["name"] for repo in repo_dicts]  # Extract repository names
stars = [repo["stargazers_count"] for repo in repo_dicts]  # Extract star counts
repo_urls = [repo["html_url"] for repo in repo_dicts]  # Extract repository URLs

# Prepare repository links for the visualization, creates clickable links for each repository
# zip(repo_urls, repo_names) returns an iterator of tuples containing (url, name) pairs
repo_links = [f"<a href='{url}' target='_blank'>{name}</a>" for url, name in zip(repo_urls, repo_names)]

# Prepare hover text for the visualization
hover_texts = []  # Initialize an empty list for hover text
for repo in repo_dicts :
    owner = repo['owner']['login']  # Extract owner's username
    description = repo['description'] if repo['description'] else "No description provided"  # Extract description
    hover_texts.append(f"{owner}<br />{description}")  # Create hover text with owner and description

# Prepare title and labels for the visualization
title = "Most-Starred Python Projects on GitHub"
labels = {
    "x": "Repository Name",
    "y": "Stars",
}

# Create a bar chart using Plotly Express
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts,)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)

# Show the figure
fig.show()