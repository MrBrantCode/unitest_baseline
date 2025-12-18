"""
QUESTION:
Implement an in-place modified version of the quicksort algorithm to sort an array in descending order without using recursion or additional data structures, and achieve a time complexity of O(n log n) and a space complexity of O(1). The function should be named `quicksort_descending` and take an array `arr` as input.
"""

def quicksort_descending(arr):
    def partition(low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] >= pivot:
                i += 1
            while i <= j and arr[j] <= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    stack = [len(arr)-1, 0]

    while stack:
        low = stack.pop()
        high = stack.pop()

        if low < high:
            pivot_index = partition(low, high)
            stack.extend([pivot_index-1, low, high, pivot_index+1])

    return arr