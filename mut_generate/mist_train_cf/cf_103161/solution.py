"""
QUESTION:
Implement the factorial2 function to calculate the factorial of a given number n using recursion. The function should have a base case to handle n = 0, and recursively call itself with a smaller value of n until it reaches the base case.
"""

def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)