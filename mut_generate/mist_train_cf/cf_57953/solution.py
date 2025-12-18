"""
QUESTION:
Given an `m x n` matrix `mat` and two integers `lowerThreshold` and `upperThreshold`, find the maximum side-length of a square with a sum less than or equal to `upperThreshold` and the minimum side-length of a square with a sum greater than or equal to `lowerThreshold`. If there is no such square, return 0 for that case.

Write a function named `maxLowerAndMinUpperSquare` that takes `mat`, `lowerThreshold`, and `upperThreshold` as input and returns a list containing the maximum side-length of the square with sum less than or equal to `upperThreshold` and the minimum side-length of the square with sum greater than or equal to `lowerThreshold`.

Constraints: `1 <= m, n <= 300`, `m == mat.length`, `n == mat[i].length`, `0 <= mat[i][j] <= 10000`, `0 <= lowerThreshold, upperThreshold <= 10^5`.
"""

def maxLowerAndMinUpperSquare(mat, lowerThreshold, upperThreshold):
    m, n = len(mat), len(mat[0])
    
    # prefix sum
    prefix = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]

    def check(mid, threshold, isLower):
        # check if there is a square submatrix with sum <= threshold when isLower = True 
        # otherwise, check if there is a square submatrix with sum >= threshold
        for i in range(mid, m+1):
            for j in range(mid, n+1):
                total = prefix[i][j] - prefix[i-mid][j] - prefix[i][j-mid] + prefix[i-mid][j-mid]
                if (isLower and total <= threshold) or (not isLower and total >= threshold):
                    return True
        return False

    # binary search for solution
    l, r = 1, min(m, n) + 1
    upper, lower = 0, 0
    # find maxLower
    while l < r:
        mid = l + (r - l) // 2
        if check(mid, upperThreshold, True):
            l = mid + 1
            upper = mid
        else:
            r = mid
    # find minUpper
    l, r = 1, min(m, n) + 1
    while l < r:
        mid = l + (r - l) // 2
        if check(mid, lowerThreshold, False):
            r = mid
            lower = mid
        else:
            l = mid + 1
    # if there is no valid upper or lower, it will be 0
    return [upper, lower]