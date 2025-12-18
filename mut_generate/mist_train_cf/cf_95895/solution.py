"""
QUESTION:
Implement a recursive function `find_max(arr)` that finds the maximum value in an array and returns the maximum value along with the total number of comparisons made. The function should handle the case when the array is empty and the array should have at least one element. The function should not use any loops.
"""

def find_max(arr):
    if len(arr) == 0:  # Handle empty array case
        return None, 0
    
    if len(arr) == 1:  # Base case when array has only one element
        return arr[0], 0
    
    mid = len(arr) // 2  # Find the middle index of the array
    
    # Recursive calls to find maximum in the left and right halves of the array
    left_max, left_comp = find_max(arr[:mid])
    right_max, right_comp = find_max(arr[mid:])
    
    # Compare the maximums found in the left and right halves
    if left_max > right_max:
        return left_max, left_comp + right_comp + 1
    else:
        return right_max, left_comp + right_comp + 1