"""
QUESTION:
Write a function named `get_name` that takes three parameters: `primary_appellation`, `secondary_designation`, and `family_name`. The function should return a string in the format: `secondary_designation` + space + first character of `primary_appellation` + '.' + space + `family_name`.
"""

def get_name(primary_appellation, secondary_designation, family_name):
    return secondary_designation + ' ' + primary_appellation[0] + '. ' + family_name