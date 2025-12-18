"""
QUESTION:
Write a recursive function `remainder(num)` that calculates the remainder of `num` divided by 4 without using the modulo operator. The function should return the remainder value.
"""

def remainder(num):
    if num < 4:
        return num
    else:
        return remainder(num - 4)