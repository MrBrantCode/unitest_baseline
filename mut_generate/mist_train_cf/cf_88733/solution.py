"""
QUESTION:
Create a function named `string_to_sorted_list` that takes a string `s` as input. The function should return a list of characters from the string, where each character is represented as a string, sorted in descending order. The solution must have a time complexity of O(n log n), where n is the length of the string.
"""

def string_to_sorted_list(s):
    char_list = list(s)
    char_list.sort(reverse=True)
    sorted_list = [str(char) for char in char_list]
    return sorted_list