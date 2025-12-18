"""
QUESTION:
Create a function called `bubbleSort` that sorts an input array in descending order using the bubble sort algorithm. The function should have a time complexity of O(n^2), where n is the number of elements in the array, and a space complexity of O(1), meaning no extra data structures can be used. Do not use any built-in sorting functions or libraries. The function should return the sorted array.
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr