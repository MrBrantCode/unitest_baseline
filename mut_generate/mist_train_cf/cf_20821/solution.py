"""
QUESTION:
Generate a function called `generate_array(N)` that creates an N x N two-dimensional array with all elements initially set to 1, where N is an integer between 3 and 10 (inclusive). The elements on the diagonal from the top left to the bottom right should be set to a unique integer starting from 2. The resulting array should have unique sums of elements for each row and column, and the time complexity of the solution should be O(N^2).
"""

def generate_array(N):
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