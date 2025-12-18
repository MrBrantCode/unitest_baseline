"""
QUESTION:
Create a function `solve(t)` that takes an input tuple `t` containing unique integers and returns a tuple. The first element of the returned tuple should be a tuple of integers from the input tuple sorted in descending order, and the second element should be a list of their original indices in the input tuple. Implement a custom sorting algorithm (quicksort, mergesort, heapsort, or bubblesort) without using the built-in sorted function.
"""

def solve(t):
    def bubble_sort(arr):
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)
        swapped = True
        
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if arr[i - 1] > arr[i]:
                    swap(i - 1, i)
                    swapped = True
                    
        return arr

    mem = list(t)
    sorted_tuple = tuple(bubble_sort(list(t)))
    indices = [mem.index(i) for i in sorted_tuple]
    return (sorted_tuple[::-1], indices[::-1])