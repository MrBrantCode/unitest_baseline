"""
QUESTION:
Write a function `findMinMax(arr, low, high)` that finds the minimum and maximum values in an unsorted array `arr` within the indices `low` and `high`. The function should use a divide-and-conquer approach to avoid comparing each element with every other element. The algorithm should adapt to the order of the elements, meaning its performance should change based on the sorted order of the input array. The input array can be of any size, and the function should handle edge cases such as arrays of length 1 or 2.
"""

def findMinMax(arr, low, high):
    if high == low:
        return (arr[low], arr[high])
    
    if high == low + 1:
        if arr[low] > arr[high]:
            return (arr[high], arr[low])
        else:
            return (arr[low], arr[high])
        
    mid = (high + low) // 2
    lmin, lmax = findMinMax(arr, low, mid)
    rmin, rmax = findMinMax(arr, mid+1, high)
    
    return (min(lmin, rmin), max(lmax, rmax))