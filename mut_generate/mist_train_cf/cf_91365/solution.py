"""
QUESTION:
Write a function named `bubble_sort` that sorts an array of numbers in descending order using the bubble sort algorithm. The function should take an array as input and return the total number of comparisons and swaps made during the sorting process. Assume the input array contains at least 1000 elements.
"""

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    
    return comparisons, swaps