"""
QUESTION:
Write a function called `generate_combinations` that takes a string `chars` as input. The function should return all possible combinations of the characters in `chars`, where each combination contains at least one uppercase letter, one lowercase letter, one number, and one special character. The combinations should be sorted in lexicographical order. The input string `chars` can contain upper and lower case letters, numbers, and special characters.
"""

import itertools

def generate_combinations(chars):
    uppercase = [c for c in chars if c.isupper()]
    lowercase = [c for c in chars if c.islower()]
    numbers = [c for c in chars if c.isdigit()]
    specials = [c for c in chars if not c.isalnum()]

    combinations = []

    for u in uppercase:
        for l in lowercase:
            for n in numbers:
                for s in specials:
                    combination = ''.join([u, l, n, s])
                    remaining_chars = ''.join([c for c in chars if c not in combination])
                    sub_combinations = generate_combinations_helper(remaining_chars)
                    for sub_combination in sub_combinations:
                        combinations.append(combination + sub_combination)

    combinations.sort()

    return combinations


def generate_combinations_helper(chars):
    if len(chars) < 4:
        return []

    combinations = []

    for r in range(4, len(chars) + 1):
        for combination in itertools.combinations(chars, r):
            combinations.append(''.join(combination))

    return combinations