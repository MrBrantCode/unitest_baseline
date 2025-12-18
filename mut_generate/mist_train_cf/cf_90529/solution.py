"""
QUESTION:
Implement a function `modified_quicksort` that sorts a list of integers in descending order using the quicksort algorithm with a time complexity of O(n log n) without using recursion or additional data structures. The function should take a list of integers as input and return the sorted list.
"""

def modified_quicksort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        pivot = arr[low]
        i = low + 1
        j = high

        while i <= j:
            while i <= j and arr[i] >= pivot:
                i += 1
            while i <= j and arr[j] < pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        stack.append((low, j - 1))
        stack.append((j + 1, high))

    return arr