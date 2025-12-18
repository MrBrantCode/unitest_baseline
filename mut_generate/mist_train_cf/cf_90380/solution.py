"""
QUESTION:
Write a function `find_locality(pin_code: str) -> str` that takes a string `pin_code` as input and returns the corresponding locality for that pin code. The pin code must be a valid Indian pin code, which is a 6-digit number. The function should return the locality name as a string, or "Locality not found" if the pin code is not found. The function should handle both upper and lower case input for the pin code, be case-sensitive for the locality names, handle leading and trailing whitespaces in the pin code and locality names, and handle non-alphanumeric characters in the pin code.
"""

def find_locality(pin_code: str) -> str:
    localities = {
        '110001': 'Connaught Place',
        '110002': 'Indraprastha',
        '110003': 'Chanakyapuri',
        '110004': 'Paharganj',
        # More locality entries...
    }

    pin_code = pin_code.strip()

    if len(pin_code) != 6 or not pin_code.isdigit():
        return 'Locality not found'

    locality = localities.get(pin_code)

    if locality is None:
        return 'Locality not found'
    else:
        return locality