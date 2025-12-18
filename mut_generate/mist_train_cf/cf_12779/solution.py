"""
QUESTION:
Create a function `check_zip_code` that takes a string `zip_code` as input and returns the corresponding US state if the zip code is valid, or "Invalid zip code" if not. The function should use a dictionary to map valid zip codes to states and a regular expression to check for the US zip code pattern of exactly 5 digits.
"""

import re

# Dictionary to map zip codes to states
zip_to_state = {
    "01000": "Massachusetts",
    "10001": "New York",
    "33100": "Florida",
    # Add more zip code - state mappings here
}

def check_zip_code(zip_code):
    # Regular expression to check for a valid US zip code pattern
    pattern = r'^\d{5}$'
    if re.match(pattern, zip_code):
        state = zip_to_state.get(zip_code, "Invalid zip code")
        return state
    else:
        return "Invalid zip code"