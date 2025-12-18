"""
QUESTION:
Write a function `merge_sort(arr, count)` that implements the Merge Sort algorithm to sort an array of floating-point numbers in descending order. The function should also count the number of comparisons made during the sorting process. 

The function should take two parameters: `arr` (the input array) and `count` (the initial number of comparisons). It should return a tuple containing the total number of comparisons and the sorted array.
"""

def merge_sort(arr, count):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_count, left_half = merge_sort(left_half, count)
        right_count, right_half = merge_sort(right_half, count)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1

            k += 1
            count += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return count, arr
    else:
        return count, arr