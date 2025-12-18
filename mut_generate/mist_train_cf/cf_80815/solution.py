"""
QUESTION:
Write a function `closest_numbers` that takes a list of numbers as input and returns the two smallest numbers in ascending order. The function must have a time complexity better than O(nlogn), where n is the size of the list. The function must handle lists with at least two elements and must be able to identify the two smallest numbers even in the presence of outliers.
"""

def closest_numbers(lst):
    if len(lst) < 2:
        return None

    min1, min2 = float('inf'), float('inf')

    for x in lst:
        if x <= min1:
            min1, min2 = x, min1
        elif x < min2:
            min2 = x

    return min1, min2