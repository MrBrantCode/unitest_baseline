"""
QUESTION:
Create a function `find_longest_string(arr)` that takes an array of strings `arr` as input and returns the longest string that contains at least one uppercase letter. If there are multiple strings of the same maximum length that meet the condition, return any one of them.
"""

def find_longest_string(arr):
    longestString = ""
    
    for string in arr:
        if not any(char.isupper() for char in string):
            continue

        if len(string) > len(longestString):
            longestString = string
    
    return longestString