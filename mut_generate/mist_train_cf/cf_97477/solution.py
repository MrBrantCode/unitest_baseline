"""
QUESTION:
Find the position of each occurrence of a given substring in a string. The function should be named `find_substring_positions` and take two parameters: `string` and `substring`. It should return a list of all positions of the substring in the string. Note that the function should be case-sensitive and consider overlapping occurrences (i.e., occurrences of the substring that overlap with each other are counted as separate occurrences).
"""

def find_substring_positions(string, substring):
    positions = []
    start = -1
    while True:
        start = string.find(substring, start + 1)
        if start == -1:
            break
        positions.append(start)
    return positions