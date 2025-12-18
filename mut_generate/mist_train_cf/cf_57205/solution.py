"""
QUESTION:
Write a function `max_sublist_sum` that takes a list of integers as input and returns a tuple containing the maximum sum of a contiguous sublist and the start and end indices of this sublist. The list may contain both positive and negative integers. The function should be efficient and only make one pass over the list.
"""

def max_sublist_sum(lst):
    max_sum = current_sum = lst[0]
    start = end = 0
    temp_start = 0
    for i in range(1, len(lst)):
        if current_sum <= 0:
            current_sum = lst[i]
            temp_start = i
        else:
            current_sum += lst[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return max_sum, start, end