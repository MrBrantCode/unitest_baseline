"""
QUESTION:
Implement the bubble_sort function to sort an array of integers in ascending order without using built-in sort methods. The function should be able to handle arrays containing negative integers and zeros.
"""

def entance(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr