# Plot population data on the world map.

import json
from pygal.maps.world import World
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

population

wm = World()
wm.title = "World Populations"
wm.add('2010', world_pop)

wm.render_to_file('files/world_populations.svg')