"""
QUESTION:
Implement a recursive function `sum_positive_even` that takes an array of at least 10 integers and returns a list of tuples, where each tuple contains a positive even number from the array and its 0-based index. The function should ignore non-positive and odd numbers. The recursion should use a divide and conquer approach, splitting the array into smaller subarrays until each subarray contains only one element.
"""

def sum_positive_even(arr, start=0):
    if len(arr) == 1:  
        if arr[0] > 0 and arr[0] % 2 == 0:  
            return [(arr[0], start)]
        else:
            return []
    
    mid = len(arr) // 2
    left_sum = sum_positive_even(arr[:mid], start)
    right_sum = sum_positive_even(arr[mid:], start + mid)
    
    return left_sum + right_sum