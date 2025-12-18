"""
QUESTION:
Create a function named `sort_array` that takes an array of integers as input and returns the array sorted in descending order. The function should use a bubble sort algorithm to sort the array. Implement the sorting algorithm correctly to ensure the function produces the expected output.
"""

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr