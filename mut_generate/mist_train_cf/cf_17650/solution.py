"""
QUESTION:
Write a function `count_integers` that takes a 2D array as input and returns the count of integers that are divisible by 2 and greater than 10.
"""

def count_integers(arr):
    count = 0
    for row in arr:
        for element in row:
            if element % 2 == 0 and element > 10:
                count += 1
    return count