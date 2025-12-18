"""
QUESTION:
Write a function `find_longest_string` that takes an array of strings as input and returns the longest string in the array. If there are multiple strings with the same maximum length, return the one that appears first in the array. The input array can be empty and have duplicates, and the strings can contain uppercase and lowercase letters as well as special characters. The length of the input array can be up to 10^6.
"""

def find_longest_string(strings):
    longest_string = None
    max_length = 0
    
    for string in strings:
        if len(string) > max_length:
            longest_string = string
            max_length = len(string)
    
    return longest_string