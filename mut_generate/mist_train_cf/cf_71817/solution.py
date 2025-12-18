"""
QUESTION:
Write a function `makeLowerAndMinUpperSquare(mat, lowerThreshold, upperThreshold)` that takes a 2D matrix `mat` and two integers `lowerThreshold` and `upperThreshold` as input. The function should return a list containing two integers representing the minimum size of a square submatrix with sum greater than or equal to `lowerThreshold` and the maximum size of a square submatrix with sum less than or equal to `upperThreshold`, respectively. Use a prefix sum approach to efficiently calculate the sum of submatrices.
"""

def makeLowerAndMinUpperSquare(mat, lowerThreshold, upperThreshold):
    m, n = len(mat), len(mat[0])

    prefix = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]

    def check(mid, threshold, isLower):
        for i in range(mid, m+1):
            for j in range(mid, n+1):
                total = prefix[i][j] - prefix[i-mid][j] - prefix[i][j-mid] + prefix[i-mid][j-mid]
                if ((isLower and total <= threshold) or (not isLower and total >= threshold)):
                    return True
        return False

    l, r = 1, min(m, n) + 1
    upper, lower = 0, 0
    while l < r:
        mid = l + (r - l) // 2
        if check(mid, upperThreshold, True):
            l = mid + 1
            upper = mid
        else:
            r = mid

    l, r = 1, min(m, n) + 1
    while l < r:
        mid = l + (r - l) // 2
        if check(mid, lowerThreshold, False):
            r = mid
            lower = mid
        else:
            l = mid + 1

    return [upper, lower]