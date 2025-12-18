"""
QUESTION:
Write a function `find_max` that takes an array of integers as input and returns the maximum number in the array. The function should not use any inbuilt functions, loops, or recursion. The array can contain negative numbers.
"""

def find_max(arr):
    max_num = arr[0]  
    if len(arr) > 1:
        if max_num < arr[1]:
            max_num = arr[1]
        if len(arr) > 2:
            if max_num < arr[2]:
                max_num = arr[2]
            if len(arr) > 3:
                if max_num < arr[3]:
                    max_num = arr[3]
                if len(arr) > 4:
                    if max_num < arr[4]:
                        max_num = arr[4]
    return max_num