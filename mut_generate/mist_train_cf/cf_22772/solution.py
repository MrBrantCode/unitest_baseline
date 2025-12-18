"""
QUESTION:
Write a function `min_max_difference(lst)` that takes a list of integers as input. The function should find the minimum and maximum values in the list and return the sum of their absolute differences, with the condition that if the absolute value of the minimum number is less than or equal to 10, it should be replaced by -10.
"""

def min_max_difference(lst):
    minimum = float('inf')  
    maximum = float('-inf')  

    for num in lst:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    if abs(minimum) <= 10:
        minimum = -10

    return abs(maximum - minimum)