"""
QUESTION:
Write a function named `print_evens` that takes two integers `n` and `m` as input, representing a range of numbers from `n` to `m` (inclusive), and prints all even numbers within this range using bitwise operators and recursion. The function should have a time complexity of O(m - n) and should not use loops. Note that due to Python's maximum recursion depth limit, this function may not work correctly for large ranges.
"""

def print_evens(n, m):
    if n > m:
        return
    if n & 1 == 0:
        print(n)
    print_evens(n+1, m)