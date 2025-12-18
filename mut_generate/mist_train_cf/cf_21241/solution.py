"""
QUESTION:
Implement a function named "find_median" that takes a list of integers as input and returns the median of the list. The function should count duplicates individually in the median calculation and round the result to the nearest integer. The solution should have a time complexity of O(n), where n is the length of the list, and should not use any built-in functions or libraries for mathematical calculations or sorting algorithms, or any additional data structures.
"""

def find_median(arr):
    def partition(arr, start, end):
        pivot = arr[end]
        smaller = equal = start

        for i in range(start, end):
            if arr[i] < pivot:
                arr[i], arr[smaller] = arr[smaller], arr[i]
                smaller += 1
                equal += 1
            elif arr[i] == pivot:
                arr[i], arr[equal] = arr[equal], arr[i]
                equal += 1
        
        arr[equal], arr[end] = arr[end], arr[equal]
        return equal

    def quickselect(arr, start, end, k):
        if start == end:
            return arr[start]

        pivot_index = partition(arr, start, end)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect(arr, start, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, end, k)

    n = len(arr)
    k = n // 2
    if n % 2 == 1:
        kth_smallest = quickselect(arr, 0, n - 1, k)
        return round(kth_smallest)
    else:
        kth_smallest1 = quickselect(arr, 0, n - 1, k - 1)
        kth_smallest2 = quickselect(arr, 0, n - 1, k)
        return round((kth_smallest1 + kth_smallest2) / 2)