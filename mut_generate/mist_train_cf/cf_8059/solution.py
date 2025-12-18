"""
QUESTION:
Write a function `second_smallest_odd_index(lst)` that takes a list of integers as input and returns the index of the second smallest odd element. If there are no odd elements or only one odd element in the list, the function should return -1. The input list can contain duplicate numbers and can have a length of up to 10^6 elements.
"""

def second_smallest_odd_index(lst):
    smallest_odd = float('inf')
    second_smallest_odd = float('inf')
    smallest_odd_index = -1
    second_smallest_odd_index = -1
    
    for i, num in enumerate(lst):
        if num % 2 != 0:  # check if odd
            if num < smallest_odd:
                second_smallest_odd = smallest_odd
                second_smallest_odd_index = smallest_odd_index
                smallest_odd = num
                smallest_odd_index = i
            elif num < second_smallest_odd:
                second_smallest_odd = num
                second_smallest_odd_index = i
    
    if second_smallest_odd_index == -1:
        return -1
    else:
        return second_smallest_odd_index