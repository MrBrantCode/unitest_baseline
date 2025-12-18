"""
QUESTION:
Write a function `analyze_sorting_performance(arr)` that takes a list of integers `arr` as input, where `arr` has a length between 10 and 1000, and its elements are between -1000 and 1000. The function should return a dictionary containing the number of comparisons and swaps made by each of the three sorting algorithms: Bubble Sort, Insertion Sort, and Selection Sort. If the input list is already sorted in ascending order, the function should return a dictionary with the number of comparisons and swaps as 0 for each algorithm.
"""

def analyze_sorting_performance(arr):
    # Bubble Sort
    def bubble_sort(arr):
        comparisons = 0
        swaps = 0
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                comparisons += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1
        return comparisons, swaps

    # Insertion Sort
    def insertion_sort(arr):
        comparisons = 0
        swaps = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                comparisons += 1
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            arr[j + 1] = key
        return comparisons, swaps

    # Selection Sort
    def selection_sort(arr):
        comparisons = 0
        swaps = 0
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                comparisons += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
        return comparisons, swaps

    # Check if the list is already sorted
    if sorted(arr) == arr:
        return {'Bubble Sort': (0, 0), 'Insertion Sort': (0, 0), 'Selection Sort': (0, 0)}

    # Analyze performance
    performance = {}
    performance['Bubble Sort'] = bubble_sort(arr.copy())
    performance['Insertion Sort'] = insertion_sort(arr.copy())
    performance['Selection Sort'] = selection_sort(arr.copy())

    return performance