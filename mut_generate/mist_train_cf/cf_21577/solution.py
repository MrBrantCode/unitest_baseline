"""
QUESTION:
Given two unsorted arrays of integers, create a function `mergeArrays(arr1, arr2)` to merge them into a single sorted array without using any extra space. The function should return the merged sorted array. The length of each array will not exceed 10^5 and the elements in each array will be integers ranging from -10^5 to 10^5.
"""

def mergeArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    # Step 2: Swap elements in arr1 with the minimum element in arr2
    for i in range(n):
        for j in range(m):
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
    
    # Step 4: Sort arr2 using any sorting algorithm
    arr2.sort()
    
    # Step 5-6: Merge the two arrays
    i = 0  # pointer for arr1
    j = 0  # pointer for arr2
    merged = []  # merged array
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements of arr1
    while i < n:
        merged.append(arr1[i])
        i += 1
    
    # Add remaining elements of arr2
    while j < m:
        merged.append(arr2[j])
        j += 1
    
    return merged