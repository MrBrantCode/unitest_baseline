"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reversed string without using any built-in string manipulation functions or methods. The function should only use basic string operations and loops and have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_string(input_string):
    reversed_string = ''
    for i in range(len(input_string)-1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string