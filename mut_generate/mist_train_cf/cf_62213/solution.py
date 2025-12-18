"""
QUESTION:
Create a function called `extract_specific_data` that takes a string as input. The function should return a list of words if the string contains commas or colons, dividing the string by these characters. If neither commas nor colons exist, it should return the total count of lower-case alphabetic characters with odd alphabetical indices (ord('a') = 0, ord('b') = 1, ..., ord('z') = 25) in the string.
"""

def extract_specific_data(input_string):
    if ',' in input_string:
        return input_string.split(',')
    elif ':' in input_string:
        return input_string.split(':')
    else:
        return sum(1 for ch in input_string if ch.islower() and (ord(ch) - ord('a')) % 2 != 0)