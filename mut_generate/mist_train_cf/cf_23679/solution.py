"""
QUESTION:
Implement a recursive function called `merge_sort` that sorts an array of integers using the merge sort algorithm. The function should take an array and two indices, `left` and `right`, as parameters. The function should recursively sort the left and right halves of the array and then merge them in sorted order. Assume that the input array is not null and the indices are valid.
"""

def merge_sort(array, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)

    merge(array, left, mid, right)


def merge(array, left, mid, right):
    left_array = array[left:mid + 1]
    right_array = array[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1