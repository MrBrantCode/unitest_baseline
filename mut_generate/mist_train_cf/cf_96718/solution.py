"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` of alphabetic characters with a maximum length of 100 characters, reverses it in-place without using any additional data structures or built-in reverse methods, and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    char_list = list(s)
    left = 0
    right = len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return ''.join(char_list)