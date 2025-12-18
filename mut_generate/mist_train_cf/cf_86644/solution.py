"""
QUESTION:
Implement the function `merge_and_remove_duplicates(arr1, arr2)` that merges two input arrays `arr1` and `arr2`, removes duplicates from the merged array, and returns the result in ascending order. The time complexity of the solution should be O(n log n) and the space complexity should be O(1), where n is the total number of elements in the merged array.
"""

def merge_and_remove_duplicates(arr1, arr2):
    def merge(left, right):
        i = 0
        j = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            elif left[i] > right[j]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def remove_duplicates(arr):
        if len(arr) <= 1:
            return arr

        unique_index = 0

        for i in range(1, len(arr)):
            if arr[i] != arr[unique_index]:
                unique_index += 1
                arr[unique_index] = arr[i]

        return arr[:unique_index + 1]

    merged = merge_sort(arr1 + arr2)
    result = remove_duplicates(merged)
    return result