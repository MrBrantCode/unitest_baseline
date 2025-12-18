"""
QUESTION:
Write a function `find_indices(s1, s2)` that takes two strings `s1` and `s2` as input and returns a list of indices where each character in `s2` is found in `s1`. The function should account for repeated characters in `s2` and return the indices for each occurrence. The function should have a time complexity of O(n+m), where n and m are the lengths of the input strings, and should handle strings of length up to 10^5.
"""

def entance(s1, s2):
    indices = []
    index = -1
    for char in s2:
        while True:
            try:
                index = s1.index(char, index + 1)
                indices.append(index)
            except ValueError:
                break
    return indices