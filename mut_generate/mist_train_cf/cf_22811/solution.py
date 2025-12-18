"""
QUESTION:
Create a function `find_locality(pin_code: str) -> str` that takes a string `pin_code` as input and returns the corresponding locality for that pin code. The function should adhere to the following constraints and requirements: 

- The pin code must be a valid Indian pin code, which is a 6-digit number.
- The function should return the locality name as a string.
- If the pin code is not found in the `localities` dictionary, the function should return "Locality not found".
- The function should handle both upper and lower case input for the pin code, but should be case-sensitive for the locality names.
- The function should handle leading and trailing whitespaces in the pin code and the locality names.
- The function should handle non-alphanumeric characters in the pin code and special characters in the locality names.
"""

def find_locality(pin_code: str) -> str:
    # Dictionary of pin codes and localities
    localities = {
        '110001': 'Connaught Place',
        '110002': 'Indraprastha',
        '110003': 'Civil Lines',
        '110004': 'Rashtrapati Bhavan',
        '110005': 'Karol Bagh',
        # ... add more pin codes and localities as needed
    }
    
    # Remove leading and trailing whitespaces from the pin code
    pin_code = pin_code.strip()
    
    # Check if the pin code is valid
    if not pin_code.isnumeric() or len(pin_code) != 6:
        return 'Invalid pin code'
    
    # Lookup the locality in the dictionary
    locality = localities.get(pin_code.upper())
    
    # Return the locality if found, otherwise return "Locality not found"
    return locality if locality else 'Locality not found'