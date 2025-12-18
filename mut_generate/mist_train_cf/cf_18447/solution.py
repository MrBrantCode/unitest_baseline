"""
QUESTION:
Implement a function `sort_array(arr)` that sorts a given array in descending order according to the following criteria: even numbers come before odd numbers, and for numbers with the same parity, the larger number comes first. The sorting should be done in-place without using any built-in sorting functions or additional data structures.
"""

def sort_array(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] % 2 == 0 and arr[j] % 2 == 0:
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            elif arr[i] % 2 != 0 and arr[j] % 2 != 0:
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            elif arr[i] % 2 != 0 and arr[j] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr