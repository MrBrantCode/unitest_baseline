"""
QUESTION:
Write a function `sumOfDigits` that takes a positive integer `num` as input and returns the sum of its digits, excluding any digits that are divisible by 3. The function should use recursion and have a time complexity of O(n), where n is the number of digits in the integer.
"""

def sumOfDigits(num):
    if num <= 0:
        return 0
    digit = num % 10
    if digit % 3 == 0:
        return sumOfDigits(num // 10)
    else:
        return digit + sumOfDigits(num // 10)