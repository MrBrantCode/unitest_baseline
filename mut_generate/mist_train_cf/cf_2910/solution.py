"""
QUESTION:
Create a function `get_capital(country_code)` that takes a country code (ISO 3166-1 alpha-2) as input and returns the capital of the country. If the country has multiple capitals, return the main capital. If the country code is not found, return a default value. The function should be able to handle multiple country codes and return the capitals in a sorted list. 

The input country codes will include 'US', 'CA', and 'GB', and the function should return the capitals in a sorted list. The function should use a dictionary to map country codes to their capitals.
"""

def get_capital(country_code):
    capitals = {
        'US': 'Washington, D.C.',
        'CA': 'Ottawa',
        'GB': 'London',
    }
    
    return capitals.get(country_code, 'Not Found')