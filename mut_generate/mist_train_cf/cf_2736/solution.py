"""
QUESTION:
Implement a function named `bubble_sort` that sorts a list of positive integers in increasing order. The solution should have a time complexity of O(n^2) and a space complexity of O(1), where n is the length of the list. The function should be stable, meaning elements with equal values should retain their relative order after sorting. Do not use any built-in sorting functions or libraries.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr