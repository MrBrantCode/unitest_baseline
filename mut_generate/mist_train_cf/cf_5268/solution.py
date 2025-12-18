"""
QUESTION:
Write a recursive function `sum_positive_even(arr, start=0)` that takes an array of integers as input and returns a list of tuples, where each tuple contains the value of a positive even number in the array and its 0-based index. The function should ignore non-positive even numbers and zeros, and handle arrays with at least 10 elements. The function should use a divide and conquer approach, splitting the array into smaller subarrays until the base case is reached, where the subarray contains only one element.
"""

def sum_positive_even(arr, start=0):
    if len(arr) == 1:  # Base case: subarray contains only one element
        if arr[0] > 0 and arr[0] % 2 == 0:  # Check if the element is a positive even number
            return [(arr[0], start)]
        else:
            return []
    
    mid = len(arr) // 2
    left_sum = sum_positive_even(arr[:mid], start)
    right_sum = sum_positive_even(arr[mid:], start + mid)
    
    return left_sum + right_sum