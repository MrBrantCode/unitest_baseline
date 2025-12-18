"""
QUESTION:
Write a function `absolute_value(num)` that calculates the absolute value of a given number `num` without using any built-in functions or libraries. The function should return the absolute value of `num`, which is the number without its negative sign if it is negative, or the number itself if it is already positive or zero.
"""

def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num