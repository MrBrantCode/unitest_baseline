"""
QUESTION:
Write a function called `find_substring` that takes a string and a substring as input and returns a list of indices where the substring occurs in the string. If the substring is not found, return an empty list.
"""

def find_substring(string, substring):
    indices = []
    substring_length = len(substring)
    for i in range(len(string) - substring_length + 1):
        if string[i:i+substring_length] == substring:
            indices.append(i)
    return indices