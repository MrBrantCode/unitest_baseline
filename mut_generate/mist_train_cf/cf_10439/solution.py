"""
QUESTION:
Write a function `last_occurrence(string, substring)` that returns the index of the last occurrence of `substring` in `string`. If `substring` is not found in `string`, return -1.
"""

def last_occurrence(string, substring):
    index = -1
    substring_length = len(substring)
    
    for i in range(len(string) - substring_length + 1):
        if string[i:i+substring_length] == substring:
            index = i
    
    return index