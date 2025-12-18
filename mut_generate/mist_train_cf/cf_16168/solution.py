"""
QUESTION:
Write a function called `bubble_sort` that takes a list of integers (`arr`) and a string (`order`) as input, where `order` can be either "ascending" or "descending". The function should sort the list in the specified order using the bubble sort algorithm, and return the sorted list along with the number of comparisons and swaps made during the sorting process.
"""

def bubble_sort(arr, order):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n-1):
        for j in range(0, n-i-1):
            comparisons += 1
            if order == "ascending":
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1
            elif order == "descending":
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1

    return arr, comparisons, swaps