"""
QUESTION:
Implement a function named `bubble_sort` that sorts an input array of integers in ascending order using the Bubble Sort algorithm, which repeatedly compares adjacent elements and swaps them if they are in the wrong order. The function should take one argument, `arr`, which is the input array of integers, and return the sorted array. The function should also be efficient and correct, handling the swapping of elements properly.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr