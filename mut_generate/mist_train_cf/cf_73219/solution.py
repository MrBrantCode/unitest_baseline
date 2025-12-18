"""
QUESTION:
Write a function named `binary_sum` that takes a string input representing either a single binary digit or two binary numbers separated by a space. The function should convert the binary numbers to integers, sum them up, and return the result as a binary string. If the input string does not match the required format, return "Invalid input".
"""

def binary_sum(s):
    input_list = s.split()
    if len(input_list) == 2:
        a, b = input_list
    elif len(input_list) == 1 and len(s) == 1:
        a, b = s, '0'
    else:
        return "Invalid input"
    a = int(a, 2)
    b = int(b, 2)
    result = bin(a + b)[2:]
    return result