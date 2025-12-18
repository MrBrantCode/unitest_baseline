"""
QUESTION:
Write a function named `reverse` that takes a single integer as input and returns the reversed integer. The input integer is guaranteed to be non-negative.
"""

def reverse(num): 
    reversed_num = 0
    while num > 0:
        last = num % 10
        reversed_num = (reversed_num * 10) + last
        num = num // 10
    return reversed_num