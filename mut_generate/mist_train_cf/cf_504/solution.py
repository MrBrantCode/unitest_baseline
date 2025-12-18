"""
QUESTION:
Write a function named `validate_phone_number` that takes two parameters: `phone_number` and `restricted_numbers`. The function should return `True` if the phone number is valid and `False` otherwise. 

The phone number is valid if it meets the following conditions: 
- It is in the format of XXX-XXX-XXXX, where each X represents a digit from 0-9.
- It is not in the list of restricted phone numbers.
- The country code (the first two letters of the phone number) is a valid two-letter country code according to the ISO 3166-1 alpha-2 standard.
- It does not have consecutive repeating digits (e.g. 111-111-1111).
- It does not have sequential digits (e.g. 123-456-7890 or 987-654-3210).

Assume that the country codes will be provided separately and that the function to validate the country code will be implemented elsewhere.
"""

def validate_phone_number(phone_number, restricted_numbers, valid_country_codes):
    """
    Validate a phone number based on the given conditions.

    Args:
    phone_number (str): The phone number to be validated.
    restricted_numbers (list): A list of restricted phone numbers.
    valid_country_codes (list): A list of valid country codes.

    Returns:
    bool: True if the phone number is valid, False otherwise.
    """

    # Check if the phone number is in the correct format
    if not re.match(r'^[A-Z]{2}\d{3}-\d{3}-\d{4}$', phone_number):
        return False

    # Check if the phone number is in the list of restricted numbers
    if phone_number in restricted_numbers:
        return False

    # Extract the country code from the phone number
    country_code = phone_number[:2]

    # Check if the country code is valid
    if country_code not in valid_country_codes:
        return False

    # Remove hyphens from the phone number
    digits = phone_number[2:].replace('-', '')

    # Check for consecutive repeating digits
    for i in range(len(digits) - 2):
        if digits[i] == digits[i+1] == digits[i+2]:
            return False

    # Check for sequential digits
    for i in range(len(digits) - 2):
        if abs(ord(digits[i]) - ord(digits[i+1])) == 1 and abs(ord(digits[i+1]) - ord(digits[i+2])) == 1:
            return False

    # If all checks pass, the phone number is valid
    return True