"""
QUESTION:
Write a function `next_mult_of_7` that takes a positive integer `num` as input and returns the smallest positive integer greater than `num` that is divisible by 7.
"""

def next_mult_of_7(num):
    return num + (7 - num%7)