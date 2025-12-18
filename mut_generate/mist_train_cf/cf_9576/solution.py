"""
QUESTION:
Write a function called `reverse_string` that takes an input string and returns its reverse without using any built-in string reversal functions or methods. The function should work for strings of any length.
"""

def reverse_string(input_str):
    reversed_str = ""
    for i in range(len(input_str)-1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str