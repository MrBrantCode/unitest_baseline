"""
QUESTION:
Write a function called "trailing_zeros" that takes in an integer "n" as a parameter and returns the number of trailing zeros in the factorial of "n", where "n" is a positive integer greater than 4. The function should have a time complexity of O(log n).
"""

def trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count