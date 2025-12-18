"""
QUESTION:
Design a function `min_moves_to_sort` that calculates the minimum number of adjacent swaps required to sort an array of integers in ascending order. The function should have a time complexity of O(n^2) and a space complexity of O(1), and it should handle arrays with duplicate elements. The input array is a list of integers, and the output is the minimum number of swaps required to sort the array.
"""

def min_moves_to_sort(arr):
    n = len(arr)
    numSwaps = 0

    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                numSwaps += 1
                swap = True

        if not swap:
            break

    return numSwaps