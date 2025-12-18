"""
QUESTION:
Create a function `find_overlapping_indices` that takes in two parameters: `string` and `substring`. The function should return all the indices in `string` where `substring` occurs, allowing for overlapping occurrences. The function must handle cases where `substring` contains special characters or symbols.
"""

def find_overlapping_indices(string, substring):
    indices = []
    length = len(substring)
    for i in range(len(string)-length+1):
        if string[i:i+length] == substring:
            indices.append(i)
    return indices