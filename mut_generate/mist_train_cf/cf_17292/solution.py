"""
QUESTION:
Implement a function `insertion_sort(arr, compare)` that sorts an array of integers using the insertion sort algorithm with a custom comparator function and returns the number of comparisons made during the sorting process. The function should take two parameters: `arr` (a list of integers) and `compare` (a function that compares two integers).
"""

def entance(arr, compare):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare(arr[j], key):
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons