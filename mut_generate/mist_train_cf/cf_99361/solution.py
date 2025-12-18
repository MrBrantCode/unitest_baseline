"""
QUESTION:
Create a function called `sort_descending` that takes an array of integers as input and returns the array sorted in descending order. The function should compare each element with one another and place them in the correct position in the final arrangement. The function should work for any size of input array.
"""

def sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr