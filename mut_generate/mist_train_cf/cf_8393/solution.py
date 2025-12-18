"""
QUESTION:
Write a function `find_locality(pin_code: str) -> str` that takes a string `pin_code` as input and returns the corresponding locality for that pin code. The function should handle both upper and lower case input for the pin code, leading and trailing whitespaces in the pin code and locality names, and non-alphanumeric characters in the pin code. The function should return "Locality not found" if the pin code is not found in the dictionary or if it's invalid (not a 6-digit number).
"""

def find_locality(pin_code: str) -> str:
    localities = {
        '110001': 'Connaught Place',
        '110002': 'Indraprastha',
        '110003': 'Chanakyapuri',
        '110004': 'Paharganj',
        # More locality entries...
    }

    # Remove leading and trailing whitespaces
    pin_code = pin_code.strip()

    # Check if the pin code is valid
    if len(pin_code) != 6 or not pin_code.isdigit():
        return 'Locality not found'

    # Lookup the locality name in the dictionary
    locality = localities.get(pin_code)

    if locality is None:
        return 'Locality not found'
    else:
        return locality