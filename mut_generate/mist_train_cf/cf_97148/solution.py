"""
QUESTION:
Write a function `count_occurrences` that takes a float number `num` and a nested list `nested_list` as input. Return the count of occurrences of `num` in `nested_list`, excluding occurrences within sublists. If `num` is not a valid float, return an error message.
"""

def count_occurrences(num, nested_list):
    if not isinstance(num, float):
        return "Error: Invalid float number"
    
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            continue  # ignore sublists
        
        if isinstance(item, float) and item == num:
            count += 1
    
    return count