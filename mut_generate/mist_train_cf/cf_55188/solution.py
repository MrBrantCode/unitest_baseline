"""
QUESTION:
Implement a function `sort_list(arr)` in Python that sorts a list of integers in ascending order using a sorting algorithm other than built-in Python sort or sorted functions. The function should handle empty lists and lists with miscellaneous combinations of positive and negative numbers.
"""

def sort_list(arr):
    n = len(arr) 

    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr