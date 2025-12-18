"""
QUESTION:
Implement the `quicksort` function that sorts an array of integers in ascending order using the quicksort algorithm, and a `partition` function that takes the array, start index, and end index as parameters and returns the index of the pivot element after partitioning. The `quicksort` function should call the `partition` function and recursively sort the subarrays. The array can have duplicate numbers, its length should be at least 10, and the solution should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def quicksort(arr, low, high):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                i = i + 1
            while i <= j and arr[j] >= pivot:
                j = j - 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)