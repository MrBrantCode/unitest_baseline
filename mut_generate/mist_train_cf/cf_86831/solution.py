"""
QUESTION:
Write a function named `bubble_sort` that takes an array of unique integers as input and returns the sorted array in ascending order along with the total number of swaps and comparisons performed during the sorting process. The time complexity should not exceed O(n^2) and space complexity should not exceed O(n), where n is the length of the input array. The function should be able to handle arrays with integers of up to 10^9 in value.
"""

def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    comparisons = 0
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            comparisons += 1
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return arr, swaps, comparisons