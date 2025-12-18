"""
QUESTION:
Write a function `find_sum(n)` to calculate the cumulative sum of all integers that are multiples of both 3 and 5 within the range from 1 to n (inclusive).
"""

def find_sum(n):
    total_sum = 0
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            total_sum += num
    return total_sum