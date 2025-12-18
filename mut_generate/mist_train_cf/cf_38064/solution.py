"""
QUESTION:
Given a function `chainResult(num)` that repeatedly replaces `num` with the sum of the squares of its digits until the resulting number is either 1 or 89, write a function to find the count of numbers from 1 to 10,000,000 (inclusive) for which the result of `chainResult(num)` is 89.
"""

def chainResult(num):
    while num != 1 and num != 89:
        num = sum(int(digit)**2 for digit in str(num))
    return num