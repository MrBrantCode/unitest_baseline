"""
QUESTION:
Write a function named `find_substring` that takes two parameters: `string` and `substring`. The function should return a list of starting indices of all occurrences of `substring` within `string`. If `substring` is not found in `string`, the function should return an empty list.
"""

def find_substring(string, substring):
    indices = []
    index = -1
    while True:
        index = string.find(substring, index + 1)
        if index == -1:
            break
        indices.append(index)
    return indices