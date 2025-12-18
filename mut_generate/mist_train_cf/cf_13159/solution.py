"""
QUESTION:
Write a function `swap_elements` that takes a list of integers as input. If the sum of the elements at index 0 and 1 is greater than the sum of the elements at index 3 and 4, swap the elements at index 2 and 4. Otherwise, do not swap any elements. Assume the input list always has at least 5 elements.
"""

def swap_elements(arr):
    if arr[0] + arr[1] > arr[3] + arr[4]:
        arr[2], arr[4] = arr[4], arr[2]
    return arr