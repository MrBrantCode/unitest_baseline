"""
QUESTION:
Implement a function named `reverse_string(s)` that takes an input string `s` and returns the reversed string. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    # Convert the input string into a list of characters
    char_list = list(s)
    
    # Initialize two pointers, 'start' at the beginning and 'end' at the end of the list
    start, end = 0, len(char_list) - 1

    # Reverse the list of characters in-place
    while start < end:
        # Swap the characters at 'start' and 'end'
        char_list[start], char_list[end] = char_list[end], char_list[start]

        # Move the pointers towards each other
        start += 1
        end -= 1
    
    # Convert the list of characters back into a string and return it
    return ''.join(char_list)