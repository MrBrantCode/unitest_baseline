"""
QUESTION:
Implement a function `reverse_string` that takes a string of at most 1000 lowercase letters as input and returns a new string with the same characters in reverse order. You are not allowed to use any built-in reverse functions or methods, or any built-in functions or methods that directly manipulate strings. The function must handle strings with duplicate characters correctly.
"""

def reverse_string(input_str):
    reversed_str = ''
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str