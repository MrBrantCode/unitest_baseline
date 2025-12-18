"""
QUESTION:
Write a function named `generate_subsets` that takes a string as input and returns all possible subsets of the input string. A subset of a string is any combination of its characters, including an empty string. The order of characters in the subset should be the same as in the original string. The function should be able to handle strings of any length.
"""

def generate_subsets(s):
    if len(s) == 0:
        return ['']
    else:
        results = list()
        for subset in generate_subsets(s[1:]):
            results.append(subset)
            results.append(s[0] + subset)
        return results