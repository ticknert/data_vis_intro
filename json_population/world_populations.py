# Plot population data on the world map.

import json
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle # To make the map more prettier.
from countries import get_country_code

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as file_obj:
    pop_data = json.load(file_obj)

world_pop = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            world_pop[code] = population

# Group the countries by population
pop_group_1, pop_group_2, pop_group_3 = {}, {}, {}
for cc, pop in world_pop.items():
    if pop < 10000000:
        pop_group_1[cc] = pop
    if pop > 10000000 and pop < 1000000000:
        pop_group_2[cc] = pop
    if pop > 1000000000:
        pop_group_3[cc] = pop

# See how many countries are in each group.
print(len(pop_group_1), len(pop_group_2), len(pop_group_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "World Populations, by Country"
wm.add('0-10mm', pop_group_1)
wm.add('10mm-1bn', pop_group_2)
wm.add('>1bn', pop_group_3)

wm.render_to_file('files/world_populations.svg')