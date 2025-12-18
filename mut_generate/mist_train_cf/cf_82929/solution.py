"""
QUESTION:
Write a function `minArea(matrix, target)` that finds the smallest submatrix in a given 2D numeric array `matrix` such that the cumulative total of its elements corresponds to a specified numerical `target`. The function should return the smallest submatrix that meets the condition. The input matrix `matrix` and the target `target` are non-empty and contain only positive integers. The function should have a time complexity of O(m^2n^2) and a space complexity of O(mn), where m and n are the dimensions of the matrix.
"""

def minArea(matrix, target):
    m, n = len(matrix), len(matrix[0])
    
    # build the prefix sum matrix
    prefix = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + matrix[i][j]
    
    # find the minimal submatrix where its sum equals to target
    minArea = float('inf')
    res = []
    for x1 in range(m+1):
        for y1 in range(n+1):
            for x2 in range(x1+1, m+1):
                for y2 in range(y1+1, n+1):
                    curSum = prefix[x2][y2] - prefix[x2][y1] - prefix[x1][y2] + prefix[x1][y1]
                    if curSum == target and (x2-x1)*(y2-y1) < minArea:
                        minArea = (x2-x1)*(y2-y1)
                        res = [row[y1:y2] for row in matrix[x1:x2]]
    return res