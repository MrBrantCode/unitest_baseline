"""
QUESTION:
Implement an iterative ternary search function called `ternary_search` that takes a sorted array `arr` and an element `x` as input. The function should return the index of the element if present in the array, else return -1. The function should be able to handle arrays of variable lengths, handle errors such as empty arrays, and non-numeric search elements. The function should not use any libraries or built-in functions for performing the ternary search and should be well-documented with comments.
"""

def ternary_search(arr, x):
    """
    Iterative Ternary Search function. 
    It returns index of x in given arr if present, else returns -1
    """

    #check if array is empty
    if not arr:
        return -1

    #check if x is a number
    try:
        float(x)
    except ValueError:
        return -1

    #First and last index of given list
    left, right = 0, len(arr) - 1

    while left <= right:

        #Find mid1 and mid2
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # If x is present at mid1
        if arr[mid1] == x:
            return mid1

        # If x is present at mid2
        if arr[mid2] == x:
            return mid2

        # If x is present in left one-third part
        if arr[mid1] > x:
            right = mid1 - 1

        # If x is present in right one-third part
        elif arr[mid2] < x:
            left = mid2 + 1

        # If x is present in middle one-third part
        else:
            left = mid1 + 1
            right = mid2 - 1

    #element is not present in array
    return -1