"""
QUESTION:
Write a function `second_smallest(x1, x2, x3, x4)` that takes four integers as input and returns the second smallest value among them. The function should handle cases where all input integers are equal or there are less than two distinct integers. It should also correctly handle potential errors or exceptions.
"""

def second_smallest(x1, x2, x3, x4):
    min1 = min2 = float('inf')
    for x in [x1, x2, x3, x4]:
        if x < min1:
            min2 = min1
            min1 = x
        elif x != min1 and x < min2:
            min2 = x
    if min2 == float('inf'):
        return min1
    return min2