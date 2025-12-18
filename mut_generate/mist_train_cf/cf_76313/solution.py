"""
QUESTION:
Write a function `second_smallest(numbers)` that takes an array of integers as input and returns the second smallest numerical value. The function should be able to handle an unordered dataset with possible repetitions and negative values. The function should also be efficient and able to handle large lists.
"""

def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2