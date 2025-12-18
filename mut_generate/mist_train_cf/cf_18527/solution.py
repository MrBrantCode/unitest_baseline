"""
QUESTION:
Write a function `print_spiral(arr: List[List[int]])` that takes a 2D array of integers as input and prints its elements in a clockwise spiral order starting from the top-left corner. The function should not return any value. The input array can be of any size, including empty.
"""

from typing import List

def print_spiral(arr: List[List[int]]) -> None:
    if not arr:
        return
    
    top = 0
    bottom = len(arr) - 1
    left = 0
    right = len(arr[0]) - 1
    
    while top <= bottom and left <= right:
        # Print top row
        for i in range(left, right + 1):
            print(arr[top][i], end=" ")
        top += 1
        
        # Print right column
        for i in range(top, bottom + 1):
            print(arr[i][right], end=" ")
        right -= 1
        
        if top <= bottom:
            # Print bottom row
            for i in range(right, left - 1, -1):
                print(arr[bottom][i], end=" ")
            bottom -= 1
            
        if left <= right:
            # Print left column
            for i in range(bottom, top - 1, -1):
                print(arr[i][left], end=" ")
            left += 1
    
    print()