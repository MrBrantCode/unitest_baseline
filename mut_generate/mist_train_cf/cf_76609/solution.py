"""
QUESTION:
Write a function called `ternarySearch` that takes in a sorted array `arr`, the left index `l`, the right index `r`, and a target value `x` as inputs. The function should return the index of the target value `x` in the array if found, and -1 otherwise.
"""

def ternarySearch(arr, l, r, x):
    if r >= l:
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        if x < arr[mid1]:
            return ternarySearch(arr, l, mid1-1, x)
        elif x > arr[mid2]:
            return ternarySearch(arr, mid2+1, r, x)
        else:
            return ternarySearch(arr, mid1+1, mid2-1, x)
    return -1