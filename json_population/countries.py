# In order to map country data, we need to use country codes.
# Country codes are two digits that represent each country.

from pygal.maps.world import COUNTRIES, World # This is not actually an error.

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(country):
    """Return the 2-digit pygal code given a country."""
    for code, name in COUNTRIES.items():
        if name == country:
            return code
    # If the country wasn't found in the list from pygal.maps.world
    return None