"""
QUESTION:
Create a function `sum_even_ascii` that takes a string as input and returns the sum of only the even ASCII values of its characters.
"""

def sum_even_ascii(string):
    ascii_sum = 0
    for char in string:
        ascii_value = ord(char)  
        if ascii_value % 2 == 0:  
            ascii_sum += ascii_value
    return ascii_sum