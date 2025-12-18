"""
QUESTION:
Implement a function named 'modified_quicksort' that sorts a list of integers in descending order using a modified version of the quicksort algorithm. The function should have a time complexity of O(n log n) and must not use any additional data structures or recursion. The function should be implemented as a single function without using any built-in sorting functions or libraries.
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