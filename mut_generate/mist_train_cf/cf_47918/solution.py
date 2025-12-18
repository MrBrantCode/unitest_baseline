"""
QUESTION:
Write a function named `cumulative_total(n)` that calculates the cumulative total of all even integers within the range of 0 to `n` (inclusive). The function should return the total sum of all even numbers in the given range.
"""

def cumulative_total(n):
    total = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            total += i
    return total