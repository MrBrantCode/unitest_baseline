"""
QUESTION:
Implement a function named `bubbleSort` that takes a list of decimal numbers as input and returns the list in descending order without using any built-in sort function. The function should correctly handle numbers with equal integer parts but different fractional parts, as well as negative decimal numbers.
"""

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr