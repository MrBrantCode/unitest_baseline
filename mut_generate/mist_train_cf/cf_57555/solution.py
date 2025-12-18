"""
QUESTION:
Write a function named `catalan(n)` that calculates and returns the nth Catalan number using only recursion. The function should not use any built-in functions or libraries.
"""

def catalan(n):
    # Base Case
    if n <= 1:
         return 1

    # Cataln number sum
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)

    return res