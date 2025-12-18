"""
QUESTION:
Create a function `quicksort_descending` that sorts an array of integers in descending order using the quicksort method with a time complexity of O(nlogn). The function should be able to handle arrays of any length, including those with duplicates, negative integers, and floating-point numbers. The array should be read from a CSV file with a specific format where the first row contains the number of elements and the second row contains the elements separated by commas. The sorted elements should be written to a text file separated by commas.
"""

def quicksort_descending(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort_descending(left) + [pivot] + quicksort_descending(right)