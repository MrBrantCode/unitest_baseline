"""
QUESTION:
Create a function named bubble_sort that sorts a list of integers in ascending order without using the built-in sort() method. The function should take a list of integers as input and return the sorted list. The function should be implemented using the bubble sort algorithm, which repeatedly compares adjacent elements in the list and swaps them if they are in the wrong order.
"""

def bubble_sort(arr):
    n = len(arr)
  
    for i in range(n):
        for j in range(0, n-i-1):
            
            # swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr