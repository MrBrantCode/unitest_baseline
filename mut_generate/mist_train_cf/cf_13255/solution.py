"""
QUESTION:
Create a function called `assign_and_sum` that takes a 2D array as input. The function should iterate through the array, assign 1 to all elements that are divisible by 3, and return the sum of these assigned elements. The original array should remain unchanged.
"""

def assign_and_sum(arr):
    sum_assigned = 0

    for row in arr:
        for element in row:
            if element % 3 == 0:
                sum_assigned += 1

    return sum_assigned