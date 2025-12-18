"""
QUESTION:
Create a function called `validate_zip_code` that takes a 5-digit US zip code as input and returns a string stating whether the zip code is valid and its corresponding state and major city if valid. The function should achieve a time complexity of O(1) for each validation and assume that a dictionary containing valid zip codes and their corresponding state and major city is predefined.
"""

# Define the dictionary of valid zip codes and their corresponding state and major city
zip_codes = {
    "90001": {"state": "CA", "major_city": "Los Angeles"},
    "10001": {"state": "NY", "major_city": "New York"},
    "60601": {"state": "IL", "major_city": "Chicago"},
    # Add more zip codes and their corresponding data here
}

def validate_zip_code(zip_code):
    if zip_code in zip_codes:
        state = zip_codes[zip_code]["state"]
        major_city = zip_codes[zip_code]["major_city"]
        return f"The zip code {zip_code} is valid. It corresponds to {major_city}, {state}."
    else:
        return f"The zip code {zip_code} is invalid."