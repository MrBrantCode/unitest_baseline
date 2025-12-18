"""
QUESTION:
Create a function named `swap_elements` that takes an array of integers as input. If the array has at least 6 unique elements, the sum of the elements at index 0 and 1 is greater than the sum of the elements at index 3 and 4, and the difference between the maximum and minimum values in the array is less than or equal to 10, then swap the elements at index 2 and 4. Otherwise, return the array unchanged.
"""

def swap_elements(arr):
    if len(arr) < 6:
        return arr
    
    sum_01 = arr[0] + arr[1]
    sum_34 = arr[3] + arr[4]
    diff = max(arr) - min(arr)

    if sum_01 > sum_34 and diff <= 10 and len(set(arr)) >= 6:
        arr[2], arr[4] = arr[4], arr[2]

    return arr