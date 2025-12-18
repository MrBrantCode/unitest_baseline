"""
QUESTION:
Create a function named `filter_strings` that takes a list of strings and an integer `n` as input. The function should return a new list containing only the strings that meet two conditions: the string contains both uppercase and lowercase letters, and its length is greater than or equal to `n`.
"""

def filter_strings(lst, n):
    return [string for string in lst if any(char.islower() for char in string) and any(char.isupper() for char in string) and len(string) >= n]