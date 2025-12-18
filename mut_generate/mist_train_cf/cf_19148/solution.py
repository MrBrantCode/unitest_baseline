"""
QUESTION:
Write a function called `find_greatest_number` that takes an array of integers as input and returns the greatest number in the array. If the array is empty, the function should return `None`. The array may contain both positive and negative integers.
"""

def find_greatest_number(arr):
    if len(arr) == 0:
        return None
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num