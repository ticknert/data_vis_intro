# Plot population data on the world map.

from pygal.maps.world import World

wm = World()
wm.title = "North American Populations"

wm.add("North America", {'ca': 34126000, 'mx': 113423000, 'us': 309349000})

wm.render_to_file('files/north_america.svg')