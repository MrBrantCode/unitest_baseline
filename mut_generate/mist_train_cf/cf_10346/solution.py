"""
QUESTION:
Implement a function named `insertion_sort` that takes an array of numbers as input and returns the array in descending order, along with the number of comparisons made during the sorting process. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. It should also handle edge cases such as an already sorted array or an array containing duplicate numbers.
"""

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key
    return arr, comparisons