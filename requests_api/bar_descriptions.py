# Use custom tooltips to show more detail on bar graphs.

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

style = LS('#336699', base_style=LCS)
chart = pygal.Bar(style=style, x_label_rotation=45, show_legend=False)

chart.title = "Python Projects"
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 10000, 'label': 'Description of httpie'},
    {'value': 15000, 'label': 'Description of django'},
    {'value': 20000, 'label': 'Description of flask'}
    ]

chart.add('', plot_dicts)
chart.render_to_file('files/bar_descriptions.svg')