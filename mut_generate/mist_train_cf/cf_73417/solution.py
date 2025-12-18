"""
QUESTION:
Write a function `second_smallest` that takes an array of integers as input and returns the second smallest element. The function should handle arrays containing duplicates, negative integers, and arrays with less than two elements. The function should have a time complexity of O(n). If no second smallest element exists, return 'No second smallest number.'
"""

def second_smallest(numbers):
    first_min = float('inf')
    second_min = float('inf')
    for n in numbers:
        if n < first_min:
            first_min, second_min = n, first_min
        elif first_min < n < second_min:
            second_min = n
    if second_min == float('inf'):
        return 'No second smallest number.'
    else:
        return second_min