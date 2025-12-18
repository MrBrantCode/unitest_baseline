"""
QUESTION:
Implement the function merge_sort(arr, reverse=False, key=None) that sorts the input array in ascending or descending order, handling various data types, including integers, floating-point numbers, strings, and arrays of objects, with a time complexity of O(n log n) and space complexity of O(1). The function should be able to handle duplicate values, multidimensional arrays, custom data types, and large ranges of values. The reverse parameter determines the order of sorting (ascending by default), and the key parameter allows for custom sorting based on a specific attribute or property of the objects.
"""

def merge_sort(arr, reverse=False, key=None):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], reverse, key)
    right_half = merge_sort(arr[mid:], reverse, key)
    return merge(left_half, right_half, reverse, key)

def merge(left, right, reverse, key):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (key is None and ((left[i] <= right[j]) ^ reverse)) or \
           (key is not None and ((key(left[i]) <= key(right[j])) ^ reverse)):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result