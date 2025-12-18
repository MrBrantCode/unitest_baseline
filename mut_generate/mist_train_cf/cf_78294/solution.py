"""
QUESTION:
Find the least common multiple of two numbers using the function `find_least_common_multiple(a, b)`. This function should take two integers `a` and `b` as input and return the smallest positive integer that is divisible by both `a` and `b` without a remainder. The function should not use any built-in functions or libraries for calculating the least common multiple.
"""

def find_least_common_multiple(a, b):
    num = 1
    while True:
        if num % a == 0 and num % b == 0:
            return num
        num += 1