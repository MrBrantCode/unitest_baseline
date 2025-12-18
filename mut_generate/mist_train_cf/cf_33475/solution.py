"""
QUESTION:
Implement the function `get_country_location(ta, countries)` that takes a dictionary `ta` containing metadata and a dictionary `countries` containing mappings of ISO codes and ISO3 codes to their respective locations. The function should return the location of the country based on the ISO code or ISO3 code found in the `ta` dictionary under the key "meta" and then "country". 

The function should check if the country code exists in the "iso" dictionary and return the corresponding location. If not found, it should check in the "iso3" dictionary. If the country code is not found in either dictionary, the function should return `None`.
"""

def get_country_location(ta: dict, countries: dict) -> str:
    """Returns the location of the country based on the ISO code or ISO3 code found in the 'ta' dictionary."""

    country_code = ta.get("meta", {}).get("country")

    return (
        countries["iso"].get(country_code) 
        or countries["iso3"].get(country_code)
    )