"""
QUESTION:
Implement a recursive bubble sort algorithm in Python to sort an array of strings in descending order. The array may contain duplicates and should be grouped together in the final sorted array. The function should be able to handle an array with only strings and without any numbers.
"""

def entance(arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                return False
        return True

    if is_sorted(arr):
        return arr
    else:
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return entance(arr)