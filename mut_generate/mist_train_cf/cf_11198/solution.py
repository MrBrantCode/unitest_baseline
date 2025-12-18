"""
QUESTION:
Write a recursive function `remainder(num)` to calculate the remainder when `num` is divided by 4, without using the modulo operator. The function should return the remainder of the division.
"""

def entance(num):
    if num < 4:
        return num
    else:
        return entance(num - 4)