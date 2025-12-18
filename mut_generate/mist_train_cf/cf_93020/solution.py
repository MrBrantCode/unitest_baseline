"""
QUESTION:
Write a function named `get_combinations` that takes two strings as input and returns a list of all possible combinations of characters from both strings, where the characters in each combination are in alphabetical order, and the list is sorted in lexicographical order. The length of each input string will not exceed 10 characters, and the output list should not contain any duplicate combinations.
"""

def get_combinations(string1, string2):
    # Generate all possible combinations of characters from both strings
    combinations = set(''.join(sorted(char1 + char2)) for char1 in string1 for char2 in string2)
    # Convert set to list and sort the combinations in lexicographical order
    combinations = sorted(list(combinations))
    return combinations