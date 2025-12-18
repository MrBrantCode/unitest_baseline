"""
QUESTION:
Write a function called `detect_duplicates` that takes an array of elements as input and returns `True` if the array contains duplicate elements, and `False` otherwise. The function must have a time complexity of O(n log n) and cannot use any external libraries or built-in sorting functions.
"""

def detect_duplicates(arr):
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i = i + 1
                else:
                    arr[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j = j + 1
                k = k + 1

    merge_sort(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False