"""
QUESTION:
Create a function named `merge_sort` that takes an array of unique integers between -1000 and 1000 inclusive as input and returns the array sorted in descending order. The input array can contain up to 1000 elements. The function should use recursion to achieve the sorting.
"""

def merge_sort(arr):
    def merge(arr1, arr2):
        merged = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        while i < len(arr1):
            merged.append(arr1[i])
            i += 1

        while j < len(arr2):
            merged.append(arr2[j])
            j += 1

        return merged

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)