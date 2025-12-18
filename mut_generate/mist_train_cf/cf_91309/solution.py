"""
QUESTION:
Implement a function named `reverse_string` that takes an input string of up to 10^6 characters and returns the string in reverse order. The solution should have a time complexity of O(n) and must not use any built-in string manipulation functions.
"""

def reverse_string(input_string):
    reversed_string = ''
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string