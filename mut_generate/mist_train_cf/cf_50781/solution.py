"""
QUESTION:
Write a function `get_multiples_of_3_and_5(n)` that returns all numbers between 1 and n (inclusive) that are evenly divisible by both 3 and 5, without using an explicit loop structure. The function should return a list of these numbers.
"""

def get_multiples_of_3_and_5(n):
    return [x for x in range(1, n+1) if x % 3 == 0 and x % 5 == 0]