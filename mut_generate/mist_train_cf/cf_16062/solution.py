"""
QUESTION:
Implement a function named `reverse_string(s)` that takes a string `s` as input and returns the reversed string without using any built-in string reversal methods or functions. The function should reverse the string character by character using a loop and without creating any new variables, handling special characters and whitespace correctly, and achieve a time complexity of O(n), where n is the length of the input string.
"""

def reverse_string(s):
    # Convert string to a list (strings are immutable in Python)
    str_list = list(s)

    # Set two pointers, one at the beginning and one at the end of the list
    left = 0
    right = len(str_list) - 1

    # Iterate until the pointers meet
    while left < right:
        # Swap the characters at the pointers
        str_list[left], str_list[right] = str_list[right], str_list[left]

        # Move the pointers towards the center
        left += 1
        right -= 1

    # Convert the list back to a string and return
    return ''.join(str_list)