"""
QUESTION:
Write a function called `find_maximum` that takes an array of integers as input and returns the maximum number from the array. You cannot use any built-in functions or methods that directly give you the maximum value in the array, and you cannot sort the array in any way. Your solution must have a time complexity of O(n), where n is the size of the array, and you cannot use any temporary variables to store intermediate values during the computation, except for the variable used to store the maximum value.
"""

def findMaximum(arr):
    max_num = arr[0]  # assume the first element is the maximum
    
    for num in arr:
        if num > max_num:
            max_num = num  # update the maximum number if a larger number is found
    
    return max_num