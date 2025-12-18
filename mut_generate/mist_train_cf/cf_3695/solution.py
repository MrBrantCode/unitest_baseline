"""
QUESTION:
Implement the `factorial2` function, which takes an integer `n` as input and returns the factorial of `n`, using recursion without any loops or additional helper functions. The function should have a runtime complexity of O(n) and a space complexity of O(n) due to the recursive call stack.
"""

def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial2(n-1)