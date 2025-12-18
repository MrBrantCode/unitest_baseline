"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of numbers in ascending order using the Bubble sort algorithm, without using any additional data structures or built-in sorting functions. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the length of the input array.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr