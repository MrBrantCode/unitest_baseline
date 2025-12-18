"""
QUESTION:
Write a function `fetch_elements` that takes a list of integers `arr` with at least 10 elements and a positive integer `n` as input. The function should return the first `n` unique elements from `arr` in ascending order.
"""

def fetch_elements(arr, n):
    if n <= 0:
        return []
    elif n >= len(arr):
        return sorted(arr)
    else:
        unique_elements = list(set(arr))
        unique_elements.sort()
        return unique_elements[:n]