"""
QUESTION:
Create a function `unique_sum_mult` that takes an array of integers as input and returns the product of the sum of all unique integers and the counts of unique positive and negative integers. If the array is empty, return `None`. If either positive or negative integers are absent, return the sum of unique integers. Zero is considered neither positive nor negative.
"""

def unique_sum_mult(arr):
    if len(arr) == 0:
        return None

    pos_count = len(set([i for i in arr if i > 0]))
    neg_count = len(set([i for i in arr if i < 0]))
    unique_sum = sum(set(arr))

    return unique_sum * pos_count * neg_count if pos_count and neg_count else unique_sum