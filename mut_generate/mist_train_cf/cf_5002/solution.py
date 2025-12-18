"""
QUESTION:
Write a function `string_to_sorted_list(s)` that takes a string `s` as input, converts it to a list of characters where each character is represented as a string, sorts the list in descending order, and returns the sorted list. The solution should have a time complexity of O(n log n), where n is the length of the string.
"""

def string_to_sorted_list(s):
    char_list = list(s)
    char_list.sort(reverse=True)
    return [str(char) for char in char_list]