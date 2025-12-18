"""
QUESTION:
Write a function named `second_smallest_even_element` that takes a list of integers as input and returns the second smallest even integer in the list. The function should not use any built-in functions. If the list has less than two even numbers, the function should return `None`. The function should handle negative integers.
"""

def second_smallest_even_element(l: list):
    min1, min2 = None, None
    for x in l:
        if x % 2 == 0:
            if min1 is None or x < min1:
                min2 = min1
                min1 = x
            elif (min2 is None or x < min2) and x != min1:
                min2 = x
    return min2