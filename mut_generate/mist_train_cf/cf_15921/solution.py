"""
QUESTION:
Write a function `find_max_element` that takes an array of integers as input and returns the maximum element of the array without using any comparison operators.
"""

def find_max_element(arr):
    max_val = arr[0]
    for num in arr[1:]:
        diff = max_val ^ num
        mask = diff & ~diff
        max_val = max_val ^ mask
        num = num ^ mask
        max_val = max_val ^ (max_val & num)
    return max_val