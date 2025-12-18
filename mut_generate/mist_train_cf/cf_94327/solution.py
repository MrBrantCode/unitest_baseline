"""
QUESTION:
Write a function `reverse_string(s)` that takes an input string `s` and returns the reversed string. The function should have a time complexity of O(n), reverse the string in-place, and handle Unicode characters correctly without using any additional data structures or built-in functions that directly reverse the string.
"""

def reverse_string(s):
    string_list = list(s)
    length = len(string_list)
    left = 0
    right = length - 1
    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]
        left += 1
        right -= 1
    return ''.join(string_list)