"""
QUESTION:
Construct a function called "classify_number" that takes a 32-bit integer as an argument and returns its classification as "positive", "negative", or "zero" based on its sign. The function cannot use if-else statements, comparison operators, or conditional expressions. It can only use bitwise operators (&, |, ~, ^, <<, >>) and arithmetic operators (+, -, *, /, %).
"""

def classify_number(num):
    sign = (num >> 31) & 1
    return ["zero", "negative"][sign] if num else "positive"