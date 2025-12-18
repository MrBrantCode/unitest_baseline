"""
QUESTION:
Write a function `sumOfDigits` that calculates the sum of the digits in a given positive integer, excluding any digits that are divisible by 3. The function should have a time complexity of O(n), where n is the number of digits in the integer, and it should be implemented using recursion.
"""

def sumOfDigits(num):
    if num <= 0:
        return 0
    digit = num % 10
    if digit % 3 == 0:
        return sumOfDigits(num // 10)
    else:
        return digit + sumOfDigits(num // 10)