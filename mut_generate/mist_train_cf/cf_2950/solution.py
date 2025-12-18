"""
QUESTION:
Implement a function called `merge_sort` that takes an array of strings as input and returns the array sorted in reverse alphabetical order, ignoring case sensitivity, without using any built-in sorting functions or libraries. The solution should have a time complexity of O(n log n), where n is the length of the input array.
"""

def merge_sort(arr):
    def merge(arr1, arr2):
        merged = []
        i = j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i].lower() >= arr2[j].lower():
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