"""
QUESTION:
Write a function `get_sum(n)` to calculate the sum of multiples of 15 within the range from 0 to n (inclusive), where n is a given integer. The function should return the sum of these multiples.
"""

def get_sum(n):
    sum = 0
    for i in range(0, n+1):
        if i % 15 == 0:
            sum += i
    return sum