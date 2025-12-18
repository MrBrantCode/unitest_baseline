"""
QUESTION:
Write a function `validate_zip_code` that checks if a given US zip code is valid and returns the corresponding state. Additionally, it should validate if the zip code corresponds to a major city within the state. The function should be able to handle a large number of zip code validations efficiently, with a time complexity of O(1) for each validation.
"""

def validate_zip_code(zip_code):
    """
    Validate a US zip code and return the corresponding state and major city.

    Args:
    zip_code (str): The zip code to be validated.

    Returns:
    str: A message indicating whether the zip code is valid and its corresponding state and major city.
    """
    zip_codes = {
        "90001": {"state": "CA", "major_city": "Los Angeles"},
        "10001": {"state": "NY", "major_city": "New York"},
        "60601": {"state": "IL", "major_city": "Chicago"},
        # Add more zip codes and their corresponding data here
    }
    if zip_code in zip_codes:
        state = zip_codes[zip_code]["state"]
        major_city = zip_codes[zip_code]["major_city"]
        return f"The zip code {zip_code} is valid. It corresponds to {major_city}, {state}."
    else:
        return f"The zip code {zip_code} is invalid."