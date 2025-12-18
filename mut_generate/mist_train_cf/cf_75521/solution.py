"""
QUESTION:
Write a function `second_smallest_odd_element` that takes a list of integers as input and returns the second smallest odd integer in the list. If no such integer exists, return None. The function should correctly handle negative integers and duplicate numbers.
"""

def second_smallest_odd_element(lst: list):
    min1 = min2 = float('Inf')
    for x in lst:
        if x % 2 != 0:
            if x <= min1:
                if x < min1:
                    min2 = min1
                min1 = x  
            elif x < min2:
                min2 = x
    return min2 if min2 < float('Inf') else None