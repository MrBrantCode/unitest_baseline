"""
QUESTION:
Write a function `reverse_string` that takes an input string as an argument and returns the string in reverse order without using any built-in string manipulation functions. The function should have a time complexity of O(n), where n is the length of the input string, and should be able to handle strings up to 10^6 characters long.
"""

def reverse_string(input_string):
    reversed_string = ''
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string