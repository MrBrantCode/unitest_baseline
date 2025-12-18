"""
QUESTION:
Create a function `check_zip_code` that takes a US zip code as a string and returns the corresponding state. The function should first validate the zip code using the standard US zip code pattern (five digits) and then return the state if the zip code is valid, or "Unknown" if the zip code is valid but not in the provided mapping, or "Invalid zip code" if the zip code is not in the standard US zip code pattern. The function should utilize a dictionary that maps each valid zip code to its corresponding state, which will be provided separately.
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
    """
    This function takes a US zip code as a string, validates it, and returns the corresponding state.

    Args:
        zip_code (str): A US zip code as a string.

    Returns:
        str: The state corresponding to the zip code if valid, "Unknown" if the zip code is valid but not in the mapping, or "Invalid zip code" if the zip code is invalid.
    """
    pattern = r'^\d{5}$'
    if re.match(pattern, zip_code):
        state = zip_to_state.get(zip_code, "Unknown")
        return state
    else:
        return "Invalid zip code"