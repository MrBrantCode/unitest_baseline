"""
QUESTION:
Write a function named `longest_string` that takes in a list of strings as input. The function should return the longest string in the list, with ties broken by the first occurrence. If the input list is empty, return None. The input list can contain duplicate strings, and the strings can include uppercase and lowercase letters as well as special characters. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def longest_string(strings):
    if not strings:
        return None
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest