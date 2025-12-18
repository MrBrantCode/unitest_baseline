"""
QUESTION:
Write a function `kthSmallestPath` that takes two inputs: `destination`, a list of two integers representing the destination coordinates, and `k`, an integer representing the desired lexicographically smallest instruction set. The function should return a string representing the `kth` lexicographically smallest instruction set that guides Bob to the `destination`.

The `destination` list is of length 2, where both elements are between 1 and 15 (inclusive). The value of `k` is between 1 and the number of combinations of `row + column` choose `row` (inclusive), where `row` and `column` are the elements of the `destination` list. The instruction set is represented as a string, where 'H' denotes a horizontal movement (move right) and 'V' denotes a vertical movement (move down).
"""

def kthSmallestPath(destination, k):
    nCr = [[0 for _ in range(31)] for _ in range(31)]
    for i in range(31):
        nCr[i][0] = 1
        for j in range(1,i+1):
            nCr[i][j] = nCr[i-1][j-1] + nCr[i-1][j]
                        
    v, h = destination
    res = []
    for _ in range(h + v):
        if h == 0:
            res.append('V')
            v -= 1
        elif v == 0:
            res.append('H')
            h -= 1
        elif nCr[h + v - 1][h - 1] < k:
            res.append('V')
            v -= 1
            k -= nCr[h + v][h]
        else:
            res.append('H')
            h -= 1
    return "".join(res)