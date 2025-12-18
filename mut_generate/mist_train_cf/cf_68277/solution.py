"""
QUESTION:
Create a function `validate_ssn(ssn)` that takes a string `ssn` as input and returns a boolean value indicating whether the social security number is valid. The social security number is considered valid if it has a length of 9 characters and only contains digits. Alternatively, it can also be valid if it is formatted as xxx-xx-xxxx, where each part is a digit string of lengths 3, 2, and 4, respectively. The function should not check whether the social security number is authentic or legitimate.
"""

def validate_ssn(ssn):
    # Social Security Number in USA is 9 digits
    # We can expand this concept to include formatting checks as well
    if len(ssn) == 9 and ssn.isdigit():
        return True
    else:
        # Social Security Number in USA is formatted as xxx-xx-xxxx
        parts = ssn.split("-")
        correct_lengths = [3, 2, 4]
        return len(parts) == 3 and all(part.isdigit() and len(part) == correct for part, correct in zip(parts, correct_lengths))