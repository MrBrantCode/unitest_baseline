"""
QUESTION:
Implement a function named "recursive" that takes an integer input "n" and returns the sum of all numbers from 1 to "n" if "n" is positive, and the sum of all numbers from "n" to 1 if "n" is negative. The function should have a time complexity of O(n) and handle the case when "n" is zero.
"""

def recursive(n):
    if n > 0:
        if n == 1:
            return 1
        else:
            return n + recursive(n - 1)
    elif n < 0:
        if n == -1:
            return -1
        else:
            return n + recursive(n + 1)
    else:
        return 0