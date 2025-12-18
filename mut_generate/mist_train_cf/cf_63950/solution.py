"""
QUESTION:
Implement a function `bubbleSort` that takes a list of integers and a string representing the order ("asc" or "desc") as input, and returns the sorted list along with the number of comparisons and swaps performed. The function should sort the list in-place using the Optimized Bubble Sort algorithm, and it should terminate early if no swaps are made in a pass, indicating the list is already sorted. If the order parameter is not provided, it should default to "asc" for ascending order.
"""

def bubbleSort(arr, order="asc"):
    n = len(arr)
    swap_count = 0
    comparison_count = 0

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            comparison_count += 1

            if order == "asc":
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_count += 1
                    swapped = True
            else:
                if arr[j] < arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_count += 1
                    swapped = True

        if not swapped:
            break

    return arr, swap_count, comparison_count