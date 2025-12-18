"""
QUESTION:
Write a function named `countdown(n)` that prints the numbers from `n` down to 1 using recursion. The function should not take any additional arguments other than `n`, and it should not use any loops. The function should handle the case where `n` is less than or equal to 0.
"""

def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)