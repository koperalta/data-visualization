import requests

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

# Explore information about the repositories
repo_dicts = response_dict['items'] # Get the list of repositories from the response
print(f"Repositories returned: {len(repo_dicts)}") # Print the number of repositories returned

# Examine each repository
print(f"\nSelected information about each repository:") # Print a header for the repository information
for repo_dict in repo_dicts :
    print(f"\nName: {repo_dict['name']}") # Print the name of the repository
    print(f"Owner: {repo_dict['owner']['login']}") # Print the owner's username
    print(f"Stars: {repo_dict['stargazers_count']}") # Print the number of stars
    print(f"Repository: {repo_dict['html_url']}") # Print the URL of the repository
    print(f"Created: {repo_dict['created_at']}") # Print the creation date of the repository
    print(f"Updated: {repo_dict['updated_at']}") # Print the last updated date of the repository
    print(f"Description: {repo_dict['description']}") # Print the description of the repository