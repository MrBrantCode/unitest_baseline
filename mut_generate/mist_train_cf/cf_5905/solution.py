"""
QUESTION:
Write a function named `find_kth_largest` that takes an unsorted array of unique positive integers and an integer k as input, and returns the kth largest element in the array. The array will contain at most 10^5 elements, with values ranging from 1 to 10^9. The function should run in an average time complexity of O(n).
"""

def find_kth_largest(arr, k):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    def quickselect(low, high, k):
        if low <= high:
            pivot_index = partition(low, high)
            if pivot_index == k-1:
                return arr[pivot_index]
            elif pivot_index < k-1:
                return quickselect(pivot_index+1, high, k)
            else:
                return quickselect(low, pivot_index-1, k)

    n = len(arr)
    return quickselect(0, n-1, k)