"""
QUESTION:
Construct a function called "classify_number" that takes an integer as an argument and returns a string classification as "positive", "negative", or "zero" based on the value of the input integer. The implementation should have a constant time complexity of O(1) and only use bitwise operators, arithmetic operators, and logical operators, without any comparison operators or if-else statements.
"""

def classify_number(num):
    sign = (num >> 31) & 1
    positive = sign & 0
    negative = sign & 1
    zero = (~sign + 1) & 0
    return "positive" * positive + "negative" * negative + "zero" * zero