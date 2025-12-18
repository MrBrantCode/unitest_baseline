"""
QUESTION:
Design a function `min_moves_to_sort` that computes the minimum number of moves required to sort an array of integers in ascending order, where a move is defined as swapping two adjacent elements. The function should be able to handle arrays with duplicate elements, have a time complexity of O(n^2), and a space complexity of O(1).
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