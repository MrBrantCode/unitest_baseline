"""
QUESTION:
Write a function `image_sharpener` that takes a 2D integer matrix `M` representing a grayscale image as input, and returns a new 2D integer matrix where the grayscale value of each cell is enhanced by increasing its value and the values of its surrounding cells by a factor of 1.5 (rounding down). The enhancement should be applied to each cell and its 8 surrounding cells (if they exist). The grayscale values in the input matrix are in the range [0, 255] and the length and width of the matrix are in the range [1, 150].
"""

def image_sharpener(M):
    if not M: 
        return []
    m, n, res = len(M), len(M[0]),[[0]* len(M[0]) for _ in range(len(M))]
    for i in range(m):
        for j in range(n):
            count = 0
            for I in range(max(0, i-1), min(i+2, m)):
                for J in range(max(0, j-1), min(j+2, n)):
                    res[i][j] += M[I][J]
                    count += 1
            res[i][j] = min(255, int(res[i][j]*1.5/count))
    return res