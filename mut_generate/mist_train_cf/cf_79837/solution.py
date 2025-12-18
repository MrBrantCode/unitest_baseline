"""
QUESTION:
Implement a function named `binary_search` that takes an integer `n` as input and checks if it is between 1 and 1000 (inclusive) using a binary search algorithm. The function should return `True` if the number is in the range, `False` otherwise, and handle non-numeric and out-of-range inputs by returning an error message. The function should not use traditional if-else conditionals to determine the range, but instead use a creative approach to mimic a switch-case structure.
"""

def binary_search(n, start=1, end=1000):
    if not str(n).isnumeric():
        return "Invalid input: must be a number"
    elif n < start or n > end:
        return "Invalid input: number out of range"
    
    while start <= end:
        mid = (start + end) // 2
        if mid < n:
            start = mid + 1
        elif mid > n:
            end = mid - 1
        else:
            return True  # The number is in the range
        
    return False  # The number is not in the range