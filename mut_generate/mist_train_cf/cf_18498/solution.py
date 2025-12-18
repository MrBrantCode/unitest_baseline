"""
QUESTION:
Write a recursive function called factorial2 that takes a non-negative integer n as input and returns the factorial of n (denoted as n!). The factorial of a number is the product of all positive integers less than or equal to that number. The implementation should have a runtime complexity of O(n) and a space complexity of O(n).
"""

def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)