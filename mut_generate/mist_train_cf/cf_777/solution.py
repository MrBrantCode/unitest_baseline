"""
QUESTION:
Create a function called `modified_insertion_sort` that sorts an array in descending order using a modified version of insertion sort, where only one comparison and one swap operation are allowed per iteration.
"""

def modified_insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and current > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr