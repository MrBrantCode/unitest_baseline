"""
QUESTION:
Write a function `rotate_matrix` that takes a 2D square array `mat` and an integer `n` as inputs, and returns the array rotated `n` times in a clockwise direction. The rotation should be performed in-place and preserve the original matrix structure. The input matrix is a square matrix (i.e., the number of rows is equal to the number of columns).
"""

def rotate_matrix(mat, n):
    for _ in range(n):
        if not mat:
            return []
        top = 0 
        bottom = len(mat)-1

        left = 0
        right = len(mat[0])-1

        while left < right and top < bottom:

            prev = mat[top+1][left]

            for i in range(left, right+1):
                curr = mat[top][i]
                mat[top][i] = prev
                prev = curr

            top += 1

            for i in range(top, bottom+1):
                curr = mat[i][right]
                mat[i][right] = prev
                prev = curr

            right -= 1

            for i in range(right, left-1, -1):
                curr = mat[bottom][i]
                mat[bottom][i] = prev
                prev = curr

            bottom -= 1

            for i in range(bottom, top-1, -1):
                curr = mat[i][left]
                mat[i][left] = prev
                prev = curr

            left += 1
    
    return mat