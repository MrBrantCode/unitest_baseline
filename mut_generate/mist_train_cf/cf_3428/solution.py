"""
QUESTION:
Write a function `extract_country_code(phone_number)` that takes a string representing a phone number as input and returns the country code as a string. The country code is the two-digit code at the beginning of the phone number, either immediately after the plus sign or enclosed in parentheses. The phone number can contain additional spaces or dashes that should be ignored. The function should have a time complexity of O(n), where n is the length of the input phone number. If the input phone number does not contain a valid country code, the function should return `None`.
"""

def entrance(phone_number):
    # Remove all spaces and dashes from the phone number
    phone_number = phone_number.replace(" ", "").replace("-", "")

    # Check if the phone number starts with a plus sign
    if phone_number[0] == "+":
        # Check if the country code is enclosed in parentheses
        if phone_number[1] == "(":
            # Find the closing parenthesis index
            closing_parenthesis_index = phone_number.find(")")

            # Extract the country code between the parentheses
            country_code = phone_number[2:closing_parenthesis_index]
        else:
            # Extract the country code after the plus sign
            country_code = phone_number[1:3]

        # Check if the extracted country code is valid
        if country_code.isdigit() and len(country_code) == 2:
            return country_code
    return None