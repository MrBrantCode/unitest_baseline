"""
QUESTION:
Find a function `find_sum` that takes an array of numbers and a target sum as input and returns two distinct numbers from the array that add up to the target sum. If no such pair is found, return False.
"""

def find_sum(arr, num):
    arr_set = set(arr)
    for i in arr_set:
        x = num - i
        if x in arr_set and x != i:  
            return i, x
    return False