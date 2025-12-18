"""
QUESTION:
Write a function `swap_elements(arr)` that takes an array of integers as input and swaps the elements at index 2 and 4 if the following conditions are met: 
- the array contains at least 6 elements
- all elements in the array are unique
- the sum of the elements at index 0 and 1 is greater than the sum of the elements at index 3 and 4
- the difference between the maximum and minimum values in the array is less than or equal to 10. 
Return the modified array if the conditions are met, otherwise return the original array.
"""

def swap_elements(arr):
    if len(arr) < 6 or len(set(arr)) < len(arr):
        return arr
    
    sum_01 = arr[0] + arr[1]
    sum_34 = arr[3] + arr[4]
    diff = max(arr) - min(arr)

    if sum_01 > sum_34 and diff <= 10:
        arr[2], arr[4] = arr[4], arr[2]

    return arr