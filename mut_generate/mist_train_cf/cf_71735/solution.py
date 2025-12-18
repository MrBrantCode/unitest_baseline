"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts an array of integers in increasing order without using the built-in sort() function. The input array will be a combination of two arrays: one with 15 random integers between 50 and 100, and another with 20 random integers between 200 and 250.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr