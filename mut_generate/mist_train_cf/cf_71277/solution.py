"""
QUESTION:
Create a function called `find_pivot` that takes a sorted list of unique integers as input and returns the index of the "pivot" element where the sum of all elements to the left equals the average of the elements to the right. If no such element exists, return -1. The list can contain both positive and negative numbers.
"""

def find_pivot(lst):
    for i in range(len(lst)):
        # sum of all elements to the left
        left_sum = sum(lst[:i])

        # average of all elements to the right
        if len(lst[i+1:]) == 0:
            right_avg = 0
        else:
            right_avg = sum(lst[i+1:]) / len(lst[i+1:])
      
        if left_sum == right_avg:
            return i

    return -1