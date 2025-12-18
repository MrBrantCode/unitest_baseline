"""
QUESTION:
Write a function called `divide_and_conquer` that sorts an array using the Divide-and-Conquer algorithm. The function should take three parameters: the input array `arr`, and two indices `low` and `high` representing the current subarray being processed. The function should return the sorted subarray. 

The `divide_and_conquer` function should use a helper function called `merge` to merge the sorted left and right subarrays. The `merge` function should take two parameters: the sorted `left` and `right` subarrays, and return the merged sorted array. 

The function should handle the base cases where `low` is greater than `high` or `low` is equal to `high`. In these cases, the function should return an empty array or an array containing the single element at index `low`, respectively. 

Implement the `divide_and_conquer` and `merge` functions correctly to sort the input array using the Divide-and-Conquer algorithm.
"""

def divide_and_conquer(arr, low, high):
    if low > high:
        return []
    elif low == high:
        return [arr[low]]
    else:
        mid = (low + high) // 2
        left = divide_and_conquer(arr, low, mid)
        right = divide_and_conquer(arr, mid + 1, high)
        merged = merge(left, right)
        return merged

def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged