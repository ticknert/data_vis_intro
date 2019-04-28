# Create a program to issue an API call to GitHub.

import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)
# During more complex API calls, the program should check for status code == 200

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Process the results of the API call.
# print(response_dict.keys())

# Examine information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Explore information about the repositories.
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])
# We are going to visualize this data later.