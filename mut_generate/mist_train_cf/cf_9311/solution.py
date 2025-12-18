"""
QUESTION:
Write a function `bubbleSortDescending` that sorts a given list of integers in descending order using the bubble sort algorithm. The function should have a time complexity of O(n^2).
"""

def bubbleSortDescending(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr