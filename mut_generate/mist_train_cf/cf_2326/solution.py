"""
QUESTION:
Write a function sum_of_digits(n) that calculates the sum of the digits of a given positive integer n, where n is at most 10^9. The solution should have a time complexity of O(log n) and should not use any built-in string conversion/manipulation functions, recursion, or external libraries.
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    
    digit_sum = 0
    while n > 0:
        digit = n % 10
        digit_sum += digit
        n //= 10
    
    return digit_sum