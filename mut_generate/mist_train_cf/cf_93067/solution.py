"""
QUESTION:
Write a function `find_longest_string` that takes an array of strings as input and returns the longest string that contains at least one uppercase letter. If there are multiple strings of the same maximum length with at least one uppercase letter, return any one of them.
"""

def find_longest_string(arr):
    longestString = ""
    
    for string in arr:
        if not any(char.isupper() for char in string):
            continue

        if len(string) > len(longestString):
            longestString = string
    
    return longestString