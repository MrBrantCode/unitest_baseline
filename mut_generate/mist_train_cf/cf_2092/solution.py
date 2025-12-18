"""
QUESTION:
Write a function named `absolute_difference` that takes a positive integer `n` less than 10^18 as input and returns the absolute difference between `n` and its reverse as an integer. The solution should have a time complexity of O(logN) and cannot use built-in functions to reverse the number.
"""

def absolute_difference(n):
    original = n
    reverse = 0
    while n > 0:
        last_digit = n % 10
        reverse = reverse * 10 + last_digit
        n = n // 10
    return abs(original - reverse)