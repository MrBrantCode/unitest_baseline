"""
QUESTION:
Create a function named `find_overlapping_indices` that takes a `string` and a `substring` as parameters. The function should return a list of all the indices in the `string` where the `substring` occurs, considering overlapping occurrences and special characters. The function should handle cases where the `substring` contains special characters or symbols.
"""

def find_overlapping_indices(string, substring):
    indices = []
    length = len(substring)
    for i in range(len(string)-length+1):
        if string[i:i+length] == substring:
            indices.append(i)
    return indices