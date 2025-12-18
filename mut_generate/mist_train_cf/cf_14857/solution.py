"""
QUESTION:
Create a function called `segregate_array` that rearranges the elements in the input array such that all negative numbers are to the left, all positive numbers are to the right, and all zeros are in the middle. The function should take an array of integers as input and return the rearranged array.
"""

def segregate_array(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] > 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    return arr