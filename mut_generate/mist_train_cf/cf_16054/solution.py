"""
QUESTION:
Write a function named `modified_bubble_sort` that sorts the non-negative elements at even indices in a list in ascending order, while leaving the elements at odd indices and negative numbers unchanged. The input is a list of integers and the output is the modified list.
"""

def modified_bubble_sort(arr):
    n = len(arr)
    for i in range(0, n, 2):
        if arr[i] >= 0:
            for j in range(0, n - i - 2, 2):
                if arr[j] >= 0 and arr[j] > arr[j + 2]:
                    arr[j], arr[j + 2] = arr[j + 2], arr[j]
    return arr