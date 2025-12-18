"""
QUESTION:
Create a function named sum_larger_items that takes an array of positive integers as a parameter. The function should calculate the total sum of all items in the array that are larger than the previous item, and return this total sum.
"""

def sum_larger_items(arr):
    total_sum = 0
    previous_item = 0
    
    for item in arr:
        if item > previous_item:
            total_sum += item
        previous_item = item
    
    return total_sum