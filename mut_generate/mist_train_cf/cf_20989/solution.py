"""
QUESTION:
Create a function named `sum_larger_items` that takes an array of positive integers as a parameter. The function should continuously add each item to a total sum if the current item is larger than the previous item. Return the total sum of all valid items in the array. Assume the array is not empty and contains only positive integers.
"""

def sum_larger_items(arr):
    total_sum = arr[0]
    previous_item = arr[0]
    
    for item in arr[1:]:
        if item > previous_item:
            total_sum += item
        previous_item = item
    
    return total_sum