"""
QUESTION:
Design a function `reverse_string` that takes a string as input and returns its reverse. The function should not use any built-in string manipulation functions or data structures, and it must achieve a time complexity of O(n), where n is the length of the input string.
"""

def reverse_string(input_string):
    reversed_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string