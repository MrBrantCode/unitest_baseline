"""
QUESTION:
Implement a function called `merge_sort(arr, count)` that sorts an array of floating-point numbers in descending order using the Merge Sort algorithm, and also keeps track of the number of comparisons made during the sorting process. The function should take an array `arr` and a variable `count` as inputs, and return the number of comparisons and the sorted array.
"""

def merge_sort(arr, count):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, count)
        merge_sort(right_half, count)

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