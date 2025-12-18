"""
QUESTION:
Implement a function `find_smallest_largest` that takes an unsorted list of numbers as input and returns the smallest and largest numbers in the list. The function should have a time complexity of O(n log n) and must not use any built-in sorting functions.
"""

def find_smallest_largest(arr):
    def merge_min_max(min_max1, min_max2):
        return min(min_max1[0], min_max2[0]), max(min_max1[1], min_max2[1])

    def get_min_max(arr, start, end):
        if start == end:
            return arr[start], arr[end]

        mid = (start + end) // 2

        min_max1 = get_min_max(arr, start, mid)
        min_max2 = get_min_max(arr, mid + 1, end)

        return merge_min_max(min_max1, min_max2)

    if not arr:
        return None, None

    return get_min_max(arr, 0, len(arr) - 1)