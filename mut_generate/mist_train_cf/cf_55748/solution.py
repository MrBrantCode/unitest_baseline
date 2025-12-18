"""
QUESTION:
Create a function `generate_worldbank_api_url` that takes a country code or ID as input and returns a URL string for querying country-level information from World Bank data sets in JSON format. The URL should be in the format `https://api.worldbank.org/v2/country/{country}?format=json`, where `{country}` is replaced with the provided country code or ID.
"""

def generate_worldbank_api_url(country):
    """
    This function generates a URL string for querying country-level information 
    from World Bank data sets in JSON format.

    Args:
        country (str): Country code or ID.

    Returns:
        str: A URL string for querying country-level information.
    """
    base_url = "https://api.worldbank.org/v2/country/"
    return f"{base_url}{country}?format=json"