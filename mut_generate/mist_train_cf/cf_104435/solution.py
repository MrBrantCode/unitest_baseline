"""
QUESTION:
Write a function named `inverse_string` that takes an input string and returns its inverse form by reversing the order of its characters. The function must use a for loop to iterate over the input string.
"""

def inverse_string(input_string):
    inverse = ""
    for i in range(len(input_string)-1, -1, -1):
        inverse += input_string[i]
    return inverse