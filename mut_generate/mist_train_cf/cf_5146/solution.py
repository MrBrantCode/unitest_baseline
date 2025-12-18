"""
QUESTION:
Write a function called "modifiedBubbleSort" that takes a list of numbers and a sorting order ("ascending" or "descending") as input, and returns the sorted list. The function should use a recursive approach and have a time complexity of O(n^2). The function should be able to handle duplicate numbers in the list efficiently.
"""

def modifiedBubbleSort(arr, order, length):
    if length > 1:
        for i in range(length - 1):
            if (order == "ascending" and arr[i] > arr[i + 1]) or (order == "descending" and arr[i] < arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return modifiedBubbleSort(arr, order, length - 1)
    else:
        return arr