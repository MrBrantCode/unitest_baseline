"""
QUESTION:
Create a function `bubbleSort` that sorts an array of numbers in ascending order using the bubble sort algorithm. The function should take an array of numbers as input and return the sorted array. The function should not use any built-in sorting methods. The input array can contain duplicate numbers.
"""

def bubbleSort(arr):
    n = len(arr)
  
    for i in range(n-1):
  
        for j in range(0, n-i-1):
  
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
    return arr