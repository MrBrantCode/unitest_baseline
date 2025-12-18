"""
QUESTION:
Implement a function named SelectionSort that sorts an array containing both integers and strings in ascending order, considering 'a' < 'b' and 1 < 2, and also 'a' < 1. The function should not use any built-in sort functions or methods. It should work for any array of mixed data types, including integers and strings.
"""

def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if type(arr[j]) == str and type(arr[min_index]) == int:
                min_index = j
            elif type(arr[j]) == type(arr[min_index]) and arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr