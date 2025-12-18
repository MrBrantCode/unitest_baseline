"""
QUESTION:
Write a function that finds the lowest index of a predetermined substring within a given string. The function should return the index of the first occurrence of the substring if found, and -1 otherwise.
"""

def find_substring_index(string, substring, start=0, end=None):
    if end is None:
        end = len(string)
    return string.find(substring, start, end)