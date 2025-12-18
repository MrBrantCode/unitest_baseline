"""
QUESTION:
Write a function `merge_sorted_arrays` that takes two sorted arrays of integers `arr1` and `arr2` of length `n` and `m` respectively, where `n` is greater than or equal to `m`. The function should merge `arr2` into `arr1` without using any built-in sorting functions or additional space, maintaining the sorted nature of the resulting array. The merged array should be stored in `arr1`.
"""

def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays of integers into the first array without using any built-in sorting functions or additional space.
    
    Parameters:
    arr1 (list): The first sorted array of integers with length n.
    arr2 (list): The second sorted array of integers with length m, where n is greater than or equal to m.
    
    Returns:
    list: The merged and sorted array stored in arr1.
    """
    
    n = len(arr1)
    gap = n // 2
    while gap > 0:
        for index in range(gap, n):
            temp = arr1[index]
            left = index
            while left >= gap and arr1[left - gap] > temp:
                arr1[left] = arr1[left - gap]
                left -= gap
            arr1[left] = temp
        gap //= 2
        
    for i in range(len(arr2)):
        arr1.append(arr2[i])
        n = len(arr1)
        gap = n // 2
        while gap > 0:
            for index in range(gap, n):
                temp = arr1[index]
                left = index
                while left >= gap and arr1[left - gap] > temp:
                    arr1[left] = arr1[left - gap]
                    left -= gap
                arr1[left] = temp
            gap //= 2
            
    return arr1