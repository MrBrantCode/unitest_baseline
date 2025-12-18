"""
QUESTION:
Create a function named `validate_ean_codes` that takes a list of 13-digit EAN (European Article Number) codes as input and returns a dictionary with the EAN codes as keys and their validation statuses as values. Each EAN code must be checked for the following conditions: 

- it must be 13 characters long
- it must only contain digit characters
- it must adhere to a specific checksum algorithm (the sum of the digits at odd positions multiplied by 3 plus the sum of the digits at even positions, and the remainder of the result divided by 10 must be equal to the last digit).

If an EAN code fails any of these checks, the corresponding value in the output dictionary should be a string describing the error; otherwise, it should be "Valid".
"""

def validate_ean_codes(ean_codes):
    def validate_ean(ean):
        if len(ean) != 13:
            return "Invalid (Length is not equal to 13 characters)"
        if not ean.isdigit():
            return "Invalid (Contains non-digit characters)"

        odds = sum(int(ean[i]) for i in range(0, 12, 2))
        evens = sum(int(ean[i]) for i in range(1, 12, 2))
        check_digit = (10 - (odds + evens * 3) % 10) % 10
        if check_digit == int(ean[-1]):
            return "Valid"
        else:
            return f"Invalid (Checksum does not match last digit. Expected {check_digit}, got {ean[-1]})"

    return {ean: validate_ean(ean) for ean in ean_codes}