"""
QUESTION:
Write a function `count_grant_types(input_string: str) -> dict` that takes a string `input_string` as input, where the string contains grant types separated by commas and may have duplicates. The function should return a dictionary containing the count of each grant type found in the input string. Assume that the input string may be empty.
"""

def count_grant_types(input_string: str) -> dict:
    grant_types = input_string.split(", ")  
    grant_type_count = {}  

    for grant_type in grant_types:
        if grant_type in grant_type_count:
            grant_type_count[grant_type] += 1  
        else:
            grant_type_count[grant_type] = 1  

    return grant_type_count