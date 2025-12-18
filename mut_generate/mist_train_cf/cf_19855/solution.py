"""
QUESTION:
Write a function named `generate_combinations` that takes a list of characters and a minimum length as input, and returns all possible combinations of strings that can be formed using the given characters, where the length of each string is greater than or equal to the specified minimum length and contains at least one uppercase letter and one lowercase letter.
"""

import itertools

def generate_combinations(chars, min_length):
    """
    Generate all possible combinations of strings that can be formed using the given characters,
    where the length of each string is greater than or equal to the specified minimum length
    and contains at least one uppercase letter and one lowercase letter.

    Args:
        chars (list): A list of characters.
        min_length (int): The minimum length of the combinations.

    Returns:
        list: A list of valid combinations.
    """

    # Generate all possible combinations of characters
    combinations = []
    for r in range(min_length, len(chars) + 1):
        combinations.extend(itertools.permutations(chars, r))

    # Filter combinations that contain at least one uppercase and one lowercase letter
    valid_combinations = []
    for combination in combinations:
        has_lowercase = False
        has_uppercase = False
        for char in combination:
            if char.islower():
                has_lowercase = True
            elif char.isupper():
                has_uppercase = True
            if has_lowercase and has_uppercase:
                valid_combinations.append("".join(combination))
                break

    return valid_combinations