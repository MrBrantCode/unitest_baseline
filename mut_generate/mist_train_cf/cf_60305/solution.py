"""
QUESTION:
Implement a function called `sort(arr)` that sorts an array of integers using an adaptive quicksort algorithm. The algorithm should choose the pivot dynamically during runtime, switch to insertion sort when the array size is small (10 or fewer elements), and use the median-of-three method to select the pivot for optimal performance. The function should modify the input array in-place and not return anything.
"""

import random

def sort(arr):
    def insertion_sort(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i-1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def partition(arr, low, high):
        pivotIndex = get_pivot(arr, low, high)
        arr[low], arr[pivotIndex] = arr[pivotIndex], arr[low]
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                i = i + 1
            while i<=j and arr[j] >= pivot:
                j = j - 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]

        return j

    def get_pivot(arr, low, high):
        mid = (high + low) // 2
        pivot = high
        if arr[low] < arr[mid]:
            if arr[mid] < arr[high]:
                pivot = mid
        elif arr[low] < arr[high]:
            pivot = low
        return pivot

    def quick_sort(arr, low, high):
        if high - low <= 10 and low < high:
            insertion_sort(arr, low, high)
        elif low < high:
            p = partition(arr, low, high)
            quick_sort(arr, low, p - 1)
            quick_sort(arr, p + 1, high)

    quick_sort(arr, 0, len(arr) - 1)