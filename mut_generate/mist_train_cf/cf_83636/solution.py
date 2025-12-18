"""
QUESTION:
Create a function `restoreMatrix` that takes two arrays `rowSum` and `colSum` as input, representing the sums of the rows and columns of a 2D matrix. The function should return a 2D array representing any matrix that fulfills the requirements, with non-negative integers, and a size of `rowSum.length x colSum.length`. The sum of the elements in the main diagonal (from top left to bottom right) should be equal to the sum of the elements in the anti-diagonal (from top right to bottom left). If no such matrix exists, return a message indicating that it's impossible to configure such a matrix.

Constraints:
- `1 <= rowSum.length, colSum.length <= 500`
- `0 <= rowSum[i], colSum[i] <= 108`
- `sum(rows) == sum(columns)`
- Note: The requirement `sum(main diagonal) == sum(anti-diagonal)` may not be achievable in all cases.
"""

def restoreMatrix(rowSum, colSum):
    rowLen, colLen = len(rowSum), len(colSum)
    mat = [[0]*colLen for _ in range(rowLen)]
    
    for r in range(rowLen):
        for c in range(colLen):
            val = min(rowSum[r], colSum[c])
            mat[r][c] = val
            rowSum[r] -= val
            colSum[c] -= val
    
    if sum(rowSum) != 0 or sum(colSum) != 0:
        return "It's impossible to configure such a matrix!"
    
    return mat