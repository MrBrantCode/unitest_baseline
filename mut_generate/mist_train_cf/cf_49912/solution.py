"""
QUESTION:
Create a function named "lucas" that generates the nth Lucas number using recursion. The Lucas sequence starts with 2 and 1, and each subsequent number is the sum of the previous two. The function should return the nth Lucas number when given an integer n.
"""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)