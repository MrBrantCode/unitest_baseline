"""
QUESTION:
Write a function `fetch_elements` that takes two parameters: `arr` and `n`, where `arr` is an array of at least 10 integer elements and `n` is a positive integer. The function should return the first `n` unique elements from `arr` in ascending order, handling duplicate elements by removing them.
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