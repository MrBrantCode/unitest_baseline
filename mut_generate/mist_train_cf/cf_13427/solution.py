"""
QUESTION:
Write a function `replace_zeros` that takes a 2D array of characters as input. Replace each '0' entry with 'x' only if it is surrounded by at least two '1' entries horizontally or vertically. The function should return the modified 2D array.
"""

def replace_zeros(arr):
    rows = len(arr)
    cols = len(arr[0])

    def valid_one(i, j):
        if i >= 0 and i < rows and j >= 0 and j < cols:
            return arr[i][j] == '1'
        return False

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == '0':
                count = 0
                if valid_one(i-1, j):  
                    count += 1
                if valid_one(i+1, j):  
                    count += 1
                if valid_one(i, j-1):  
                    count += 1
                if valid_one(i, j+1):  
                    count += 1
                if count >= 2:
                    arr[i][j] = 'x'

    return arr