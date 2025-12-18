"""
QUESTION:
Write a function named `merge_sort` that takes an array of integers as input, and returns a new array with the elements in descending order. The function should not use any built-in sorting functions or data structures, and it should only use a constant amount of extra space. The time complexity of the function should be O(n log n), where n is the length of the input array.
"""

def merge_sort(arr):
    def merge(left, right):
        result = []
        
        while len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]

        while len(left) > 0:
            result.append(left[0])
            left = left[1:]

        while len(right) > 0:
            result.append(right[0])
            right = right[1:]

        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)