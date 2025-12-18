"""
QUESTION:
Write a function named `reverse_string(s)` that takes a string `s` consisting of at most 1000 lowercase letters and returns a new string with the same set of characters in reverse order. The function must implement its own algorithm to reverse the string character by character without using built-in reverse functions or methods, string slicing, or concatenation. The input string can be assumed to be non-empty and only contain lowercase letters.
"""

def reverse_string(s):
    char_list = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return ''.join(char_list)