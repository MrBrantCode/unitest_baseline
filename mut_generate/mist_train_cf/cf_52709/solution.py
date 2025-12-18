"""
QUESTION:
Write a function `decimal_to_binary(lst)` that takes a list of integers as input and returns a list of their binary representations as strings, without the '0b' prefix. The function should be able to handle a list of any length and any integer values.
"""

def decimal_to_binary(lst):
    return [bin(num).replace("0b", "") for num in lst]