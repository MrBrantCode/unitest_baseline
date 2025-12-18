"""
QUESTION:
Implement a function called `bubble_sort` that sorts a list of elements in either ascending or descending order. The function should take two parameters: `arr`, the list to be sorted, and `order`, the sorting order ("asc" for ascending or "desc" for descending). The function should return a tuple containing the sorted list and the total number of swaps made during the sort process.
"""

def bubble_sort(arr, order="asc"):
    n = len(arr)
    swap_count = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if (order == "asc" and arr[j] > arr[j+1]) or (order == "desc" and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1

    return arr, swap_count