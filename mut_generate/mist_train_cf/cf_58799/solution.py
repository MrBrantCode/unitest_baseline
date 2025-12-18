"""
QUESTION:
Implement a function `mergeSort` that sorts an array of integers in ascending order using the Merge Sort algorithm, ensuring a time complexity of O(N log N), and without using any built-in sort functions. After sorting, remove any duplicate values from the array and return the result. The input array is not guaranteed to be of size N, but the size constraint is 4.
"""

def mergeSort(arr):
    def merge(left, right):
        result = []
        i = j = 0
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

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    merged = merge(left, right)
    return list(dict.fromkeys(merged))  # remove duplicates and preserve order