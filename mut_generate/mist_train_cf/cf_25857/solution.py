"""
QUESTION:
Write a function `minMoves` that takes an array of integers as input and returns the minimum number of adjacent swaps required to sort the array in ascending order. The input array will contain distinct integers and the function should only perform swaps of adjacent elements.
"""

def minMoves(arr): 
    n = len(arr) 
    moves = 0
    for i in range(n):  
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:  
                temp = arr[j]
                arr[j] = arr[j + 1] 
                arr[j + 1] = temp
                moves += 1

    return moves