"""
QUESTION:
Write a function `get_combinations` that takes two strings as input and returns a list of all possible combinations of two characters, one from each string. The length of each input string will not exceed 10 characters. The output list should contain no duplicates, with characters in each combination in alphabetical order, and the combinations themselves in lexicographical order.
"""

def get_combinations(string1, string2):
    # Generate all possible combinations of characters from both strings
    combinations = set()
    for char1 in string1:
        for char2 in string2:
            combination = ''.join(sorted(char1 + char2))
            combinations.add(combination)
    # Sort the combinations in lexicographical order
    combinations = sorted(list(combinations))
    return combinations