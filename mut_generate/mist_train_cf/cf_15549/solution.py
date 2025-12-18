"""
QUESTION:
Write a function named `reverse_string` that takes a string as input, reverses the string without using any built-in string reversal functions or methods, does not use any additional data structures, and has a time complexity of O(n).
"""

def reverse_string(string):
    # Convert the string into a list of characters
    char_list = list(string)

    # Initialize start and end pointers
    start = 0
    end = len(char_list) - 1

    # Reverse the string by swapping characters
    while start < end:
        char_list[start], char_list[end] = char_list[end], char_list[start]
        start += 1
        end -= 1

    # Convert the list of characters back to a string
    reversed_string = ''.join(char_list)
    return reversed_string