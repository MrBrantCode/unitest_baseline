"""
QUESTION:
Write a function `lucas(n)` to generate the nth Lucas number, where the sequence starts with 2 and 1, and each subsequent number is the sum of the previous two. The function should handle non-negative integers n and return the correct Lucas number. Note that the function may use recursion, but it should avoid redundant calculations to handle larger inputs efficiently.
"""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b