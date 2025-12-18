"""
QUESTION:
Generate a function `generate_array(N)` where N is an integer between 3 and 10 (inclusive), to create a two-dimensional array of size N x N with the following properties: 
- All elements are initialized to 1.
- The elements in the diagonal from the top left to the bottom right are set to a unique increasing sequence starting from 2.
- Each row and column has a unique sum of elements.
The time complexity of the solution should be O(N^2).
"""

def entrance(N):
    arr = [[1] * N for _ in range(N)]
    diagonalValue = 2

    for i in range(N):
        arr[i][i] = diagonalValue
        diagonalValue += 1

    rowSum = [sum(row) for row in arr]
    colSum = [sum(col) for col in zip(*arr)]

    for i in range(N):
        for j in range(N):
            if i != j and rowSum[i] == rowSum[j]:
                arr[j][j] += 1
                rowSum[j] = sum(arr[j])
            if i != j and colSum[i] == colSum[j]:
                arr[j][j] += 1
                colSum[j] = sum(col[j] for col in arr)

    return arr