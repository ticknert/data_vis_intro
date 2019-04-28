# Create a program to issue an API call to GitHub.
# Also visualize the top Python repositories.

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)
# During more complex API calls, the program should check for status code == 200

# Store API response in a variable.
response_dict = r.json()
print("Total Repositories:", response_dict['total_count'])

# Process the results of the API call.
# print(response_dict.keys())

# Examine information about the repositories
repo_dicts = response_dict['items']

names, plot_dicts = [], []
# Explore information about the repositories.
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Get the project description, if available.
    description = repo_dict['description']
    if not description:
        description = "No description provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)

# Make the visualization as a .svg file.
style = LS('#336699', base_style=LCS)
style.title_font_size = 24
style.label_font_size = 14
style.major_label_font_size = 18

config = pygal.Config()
config.x_label_rotation = 45
config.show_legend = False
config.truncate_label = 15
config.show_y_guides = False
config.width = 1000
chart = pygal.Bar(config=config, style=style)
chart.title = "Most-Starred Python Repositories on GitHub"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('files/python_repos.svg')