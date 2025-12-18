"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns its reverse. The function cannot use built-in string manipulation functions or methods, nor can it use any built-in data structures such as lists or arrays. The function should only use basic operations like accessing individual characters and concatenation.
"""

def reverse_string(input_str):
    reversed_str = ''
    length = len(input_str)
    for i in range(length-1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str