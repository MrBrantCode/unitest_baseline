"""
QUESTION:
Write a function `second_max_min` that takes a list of numbers as input and returns a tuple containing the second maximum and second minimum numbers in the list, without using any built-in functions, libraries, or sorting algorithms.
"""

def second_max_min(numbers):
    min1, min2, max1, max2 = float('inf'), float('inf'), float('-inf'), float('-inf')
    for x in numbers:
        if x < min1:
            min1, min2 = x, min1
        elif x < min2:
            min2 = x
        if x > max1:
            max1, max2 = x, max1
        elif x > max2:
            max2 = x
    return max2, min2