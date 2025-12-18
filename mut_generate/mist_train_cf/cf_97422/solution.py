"""
QUESTION:
Write a function `divide_list` that takes a list with an even number of elements as input and returns two equal halves of the list. The list should be split at the middle index.
"""

def divide_list(lst):
    length = len(lst)
    mid = length // 2
    
    first_half = lst[:mid]
    second_half = lst[mid:]
    
    return first_half, second_half