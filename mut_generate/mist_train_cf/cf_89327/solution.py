"""
QUESTION:
Implement the function `replaceWithGreatest` that takes a 2D array of non-negative integers as input and replaces each element in the array with the greatest element found on its row. The function should run in O(n) time complexity, where n is the total number of elements in the input array, and modify the input array in-place without using any additional data structures.
"""

def replaceWithGreatest(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    for i in range(rows):
        maxRow = -1
        for j in range(cols):
            if arr[i][j] > maxRow:
                maxRow = arr[i][j]
        
        for j in range(cols):
            arr[i][j] = maxRow
    
    return arr