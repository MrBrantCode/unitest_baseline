"""
QUESTION:
Write a function `merge_sorted` that takes two arrays as input, merges them into one sorted array, and returns the merged array. The input arrays may not be sorted. 

The function should be able to handle arrays of any length, including empty arrays, and should not assume any specific length or order of elements. 

Additionally, write a function `find_median` that takes a sorted array as input and returns the median element of the array. If the array has an even number of elements, the median should be the average of the two middle elements.
"""

def merge_sorted(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    arr = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
            
    if i < len(arr1):
        arr.extend(arr1[i:])
    
    if j < len(arr2):
        arr.extend(arr2[j:])

    return arr


def find_median(arr):
    n = len(arr)
    
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]