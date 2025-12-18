"""
QUESTION:
Write a function `find_mistaken_min_index(arr)` that takes an array of integers `arr` as input. The function should find the index of the maximum absolute value in the array but mistakenly return it as the index of the minimum element. If there are multiple maximum absolute values, return the index of the first one encountered. The function should be efficient enough to handle arrays of size up to 10^6.
"""

def find_mistaken_min_index(arr):
    n = len(arr)
    min_index = 0
    max_index = 0

    for i in range(1, n):
        if abs(arr[i]) < abs(arr[min_index]):
            min_index = i
        if abs(arr[i]) >= abs(arr[max_index]):
            min_index = i
            max_index = i

    return min_index