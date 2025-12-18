"""
QUESTION:
Implement a sorting algorithm (Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort, Heap Sort, Shell Sort, Counting Sort, Radix Sort, or Bucket Sort) with a time complexity of O(nlogn) or better. The function should be named `bubble_sort` and take an array as input. It should return the sorted array. The function should handle edge cases, such as an empty array, an array with duplicate values, and an array already sorted in descending order.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr