"""
QUESTION:
Write a function named `common_elements(arr1, arr2)` that takes two arrays `arr1` and `arr2` as input and returns a list of common elements from both arrays. The function should have a time complexity of O(nlogn), where n is the size of the larger array. The function should not use any built-in functions or data structures for sorting. The input arrays should be sorted in ascending order before finding the common elements.
"""

def common_elements(arr1, arr2):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    i, j = 0, 0
    common = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            common.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return common