"""
QUESTION:
Design a function `findLongestStringLength` that takes a list of strings as input and returns the length of the longest string in the list. The function should return an integer value representing the length of the longest string. The input list can contain any number of strings, and the function should be able to handle lists of varying lengths.
"""

def findLongestStringLength(string_list):
    max_length = 0
    for s in string_list:
        if len(s) > max_length:
            max_length = len(s)
    return max_length