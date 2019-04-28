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

# Examine the first repsitory.
repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# Explore information about the repositories.
print("\nSelected information about the first repository:")
print("Name:", repo_dict['name'])
print("Owner:", repo_dict['owner']['login'])
print("Stars:", repo_dict['stargazers_count'])
print("Repository:", repo_dict['html_url'])
print("Created:", repo_dict['created_at'])
print("Updated:", repo_dict['updated_at'])
print("Description:", repo_dict['description'])