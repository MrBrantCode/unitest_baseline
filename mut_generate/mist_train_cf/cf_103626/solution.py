"""
QUESTION:
Create a function `sum_if_larger` that takes an array as a parameter. The function should continuously add each item to the total sum, but only if the current item is larger than the previous item.
"""

def sum_if_larger(arr):
    total_sum = 0
    previous_item = float('-inf')  # Set previous item to negative infinity as initial value
    
    for item in arr:
        if item > previous_item:
            total_sum += item
        previous_item = item
    
    return total_sum