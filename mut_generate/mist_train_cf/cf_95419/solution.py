"""
QUESTION:
Write a function named `reverse_string` that takes an input string and returns the string reversed. The function cannot use any built-in string manipulation functions or methods, and it cannot use built-in data structures such as lists or arrays. The function should only use basic operations such as accessing individual characters of the string and concatenation.
"""

def reverse_string(input_str):
    reversed_str = ''
    length = len(input_str)
    for i in range(length-1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str