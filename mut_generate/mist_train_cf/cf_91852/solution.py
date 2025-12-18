"""
QUESTION:
Implement a recursive function named factorial2 to calculate the factorial of a given number n, where n is a non-negative integer. The function should have a time complexity of O(n) and space complexity of O(n).
"""

def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)