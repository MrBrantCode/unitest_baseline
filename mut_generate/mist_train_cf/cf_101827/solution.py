"""
QUESTION:
Write a function named `check_characters` that checks if a given set of characters contains the character 'A' and if the set contains any duplicate characters. The function should return two boolean values: one for the presence of 'A' and one for the presence of duplicates. The function should be able to handle any set of characters, not limited to the English alphabet, and should not be responsible for storing or retrieving the set from a database or outputting the results in any specific format.
"""

def check_characters(characters):
    has_a = 'A' in characters
    has_duplicates = len(set(characters)) != len(characters)
    return has_a, has_duplicates