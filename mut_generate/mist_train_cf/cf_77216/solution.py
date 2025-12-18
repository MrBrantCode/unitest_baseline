"""
QUESTION:
Write a function named `starts_one_ends` that takes a positive integer `n` as input. The function should return the count of n-digit numbers that either start or end with 1 and are divisible by either 3 or 5, excluding those that are divisible by both 3 and 5.
"""

def starts_one_ends(n):
    count = 0
    for i in range(10 ** (n - 1), 10 ** n):
        if ((str(i)[0] == '1' or str(i)[-1] == '1') and (i % 3 == 0 or i % 5 == 0) and i % 15 != 0):
            count += 1
    return count