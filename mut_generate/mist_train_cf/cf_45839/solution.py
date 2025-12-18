"""
QUESTION:
Create a function `make_arr3(arr1, arr2)` that takes two 1D arrays `arr1` and `arr2` as input and returns a new 2D array `arr3`. The elements of `arr1` and `arr2` should be alternated in `arr3` such that the first element in each sub-array of `arr3` is from `arr1` and the second element is from `arr2`. If `arr1` and `arr2` are not of the same size, return "Invalid Input".
"""

def make_arr3(arr1, arr2):
    if len(arr1) != len(arr2):
        return 'Invalid Input'
    
    arr3 = [[arr1[i], arr2[i]] for i in range(len(arr1))]
    
    return arr3