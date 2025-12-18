"""
QUESTION:
Implement a function `quicksort_descending` that sorts the given array in descending order using an in-place modified version of the quicksort algorithm with a time complexity of O(n log n) and space complexity of O(1). The function should not use any additional data structures or recursion. It should be able to handle arrays with duplicate elements and return the sorted array.
"""

def quicksort_descending(arr):
    def partition(arr, low, high):
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

    stack = []
    stack.append(len(arr)-1)
    stack.append(0)

    while stack:
        low = stack.pop()
        high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append(pivot_index-1)
            stack.append(low)
            stack.append(high)
            stack.append(pivot_index+1)

    return arr