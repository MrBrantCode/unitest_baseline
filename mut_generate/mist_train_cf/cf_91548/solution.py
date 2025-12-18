"""
QUESTION:
Write a function `count_divisible_by_2` that takes a 2D array of integers as input and returns the count of integers in the array that are divisible by 2. The function should iterate through each element in the array and use the modulus operator to check for divisibility by 2.
"""

def count_divisible_by_2(arr):
    count = 0
    for row in arr:
        for element in row:
            if element % 2 == 0:
                count += 1
    return count