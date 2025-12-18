"""
QUESTION:
Create a function `printSpiral(m)` that takes a 2D list `m` as input and prints out each element on its own line in a spiral order. The input list can be a rectangular matrix of integers, and the function should be able to handle both square and non-square matrices.
"""

def printSpiral(m):
    if not m:
        return
    top = left = 0
    bottom = len(m)-1
    right = len(m[0])-1
    while True:
        if left>right:
            break
        # print top row
        for i in range(left, right+1):
            print(m[top][i])
        top += 1
        if top>bottom:
            break
        # print right column
        for i in range(top, bottom+1):
            print(m[i][right])
        right -= 1
        if left>right:
            break
        # print bottom row
        for i in range(right, left-1, -1):
            print(m[bottom][i])
        bottom -= 1
        if top>bottom:
            break
        # print left column
        for i in range(bottom, top-1, -1):
            print(m[i][left])
        left += 1