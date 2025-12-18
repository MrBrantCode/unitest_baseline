"""
QUESTION:
Write a function `sum_of_digits(n)` that takes a positive integer `n` as input and returns the sum of its digits. The input integer will be at most 10^9. The function must have a time complexity of O(log n) and cannot use built-in string conversion or manipulation functions, recursion, or external libraries.
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