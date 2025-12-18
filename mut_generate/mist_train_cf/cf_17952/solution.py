"""
QUESTION:
Define a function `combine_strings` that takes an array of strings as input. The function should return a single string that combines strings from the array, but only includes strings that contain both uppercase and lowercase letters, and does not contain special characters or numbers. The combined string should be sorted in descending order based on the length of each string. If no strings meet the requirements, the function should return an empty string.
"""

def combine_strings(array):
    valid_strings = [string for string in array if string.isalpha() and any(char.isupper() for char in string) and any(char.islower() for char in string)]
    valid_strings.sort(key=lambda x: len(x), reverse=True)
    return ''.join(valid_strings)