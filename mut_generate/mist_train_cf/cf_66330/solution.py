"""
QUESTION:
Generate all proper subsets of a given string, excluding the string itself and the empty set. The function should take a string as input and may use recursion. The number of subsets can be 2^n - 2, where n is the length of the string, since every character has two choices: either to be included in the subset or not.
"""

def get_subsets(s, index=0, current_subset=""):
    if index == len(s):
        if current_subset != "" and current_subset != s:
            return [current_subset]
        else:
            return []
    else:
        return get_subsets(s, index + 1, current_subset) + get_subsets(s, index + 1, current_subset + s[index])