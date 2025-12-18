"""
QUESTION:
Write a function `generate_combinations` that generates all unique combinations of a given string where each combination contains exactly 3 characters, without repetition of any characters within a combination. The order of characters in the combinations does not matter.
"""

def generate_combinations(string):
    """
    Generate all unique combinations of a given string where each combination contains exactly 3 characters,
    without repetition of any characters within a combination.

    Args:
        string (str): The input string.

    Returns:
        list: A list of all unique combinations.
    """
    combinations = set()
    for i in range(len(string)):
        for j in range(len(string)):
            for k in range(len(string)):
                if i != j and i != k and j != k:
                    combination = ''.join(sorted([string[i], string[j], string[k]]))
                    combinations.add(combination)
    return list(combinations)