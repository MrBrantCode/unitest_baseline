"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and reverses it without using any built-in functions or methods that directly reverse the string. The solution should have a time complexity of O(n) and reverse the string in-place without using any additional data structures. It should correctly handle Unicode characters and be able to handle very long strings efficiently.
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