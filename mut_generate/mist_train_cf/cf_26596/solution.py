"""
QUESTION:
Create a function `validateLicenses` that takes a list of license strings as input. Each license string must be 17 characters long, where the first 16 characters are the license key and the last character is the license type. The license key must contain at least 3 distinct numeric digits and at least 2 distinct uppercase letters, and the license type must be one of 'A', 'B', 'C', or 'D'. The function should return a list of boolean values indicating whether each license is valid or not.
"""

from typing import List

def validateLicenses(licenses: List[str]) -> List[bool]:
    def is_valid_license(license: str) -> bool:
        if len(license) != 17:
            return False
        if license[16] not in ['A', 'B', 'C', 'D']:
            return False
        digits = [char for char in license if char.isdigit()]
        letters = [char for char in license if char.isalpha() and char.isupper()]
        if len(set(digits)) < 3 or len(set(letters)) < 2:
            return False
        return True

    return [is_valid_license(license) for license in licenses]