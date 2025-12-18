"""
QUESTION:
Write a function `convert_num` that takes an integer as input and returns its negation using the bitwise NOT operator, considering Python's integer representation. The function should work for both positive and negative integers.
"""

def convert_num(num):
    return ~num + 1