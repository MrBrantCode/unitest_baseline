"""
QUESTION:
Write a function `has_pair_sum` that takes an array of integers `arr` and a target integer `k` as input. The function should return `True` if there exists a pair of numbers in `arr` that add up to `k`, and `False` otherwise. The array may contain duplicates and negative numbers.
"""

def has_pair_sum(arr, k):
    seen = set()
    for num in arr:
        if k - num in seen:
            return True
        seen.add(num)
    return False