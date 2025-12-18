"""
QUESTION:
Create a function named `find_indices` that takes two strings, `s1` and `s2`, as parameters. The function should return a list of indices in `s1` where each character from `s2` is found, accounting for repeated characters in `s2`. Note that this function should return the indices for each occurrence of a character from `s2` in `s1`.
"""

def find_indices(s1, s2):
    indices = []
    for char in s2:
        for i in range(len(s1)):
            if s1[i] == char:
                indices.append(i)
    return indices