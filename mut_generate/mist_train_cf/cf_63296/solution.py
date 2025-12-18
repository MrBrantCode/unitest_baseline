"""
QUESTION:
Write a function `unique_sum_mult` that takes an array of integers as input and returns the sum of all distinctive numbers multiplied by the product of the counts of unique positive and negative integers. If the array is empty, return `None`. Zeroes are ignored in the calculation.
"""

def unique_sum_mult(arr: list) -> int:
    # Check if array is empty
    if not arr:
        return None
    
    # Store unique positive and negative numbers
    pos = {x for x in arr if x > 0}
    neg = {x for x in arr if x < 0}

    # Compute sum of unique numbers
    total_sum = sum(pos) + sum(neg)

    # Compute product of counts of unique positive and negative integers
    total_mult = len(pos) * len(neg) if neg else len(pos)

    # Return the result
    return total_sum * total_mult