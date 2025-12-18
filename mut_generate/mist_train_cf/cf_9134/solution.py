"""
QUESTION:
Implement the `remove_duplicates_and_sort` function to sort an array in ascending order with no duplicate elements, using a sorting algorithm with a time complexity of O(n log n) and a space complexity of O(1). The function should take an array as input and return the sorted array with no duplicates.
"""

def remove_duplicates_and_sort(arr):
    arr = list(set(arr))

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

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

    arr = merge_sort(arr)
    return arr