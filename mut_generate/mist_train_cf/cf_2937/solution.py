"""
QUESTION:
Write a function named `compute_min_edits` that takes two strings `str1` and `str2` as input and returns a tuple containing the minimum number of edits required to transform `str1` into `str2` and the sequence of edits required. The edits can be insertions, deletions, or substitutions, and they should be performed in the order of deletions, insertions, and substitutions. The function should handle cases where the total number of characters in the final string does not exceed a certain limit (not specified), but for this problem, you can assume there is no limit on the final string length.
"""

def compute_min_edits(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    edits = [[''] * (n+1) for _ in range(m+1)]

    # Initialize the first row and column
    for i in range(m+1):
        dp[i][0] = i
        edits[i][0] = 'D' * i
    for j in range(n+1):
        dp[0][j] = j
        edits[0][j] = 'I' * j

    # Fill in the remaining values
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                edits[i][j] = edits[i-1][j-1]
            else:
                deletion = dp[i-1][j] + 1
                insertion = dp[i][j-1] + 1
                substitution = dp[i-1][j-1] + 1
                if deletion <= insertion and deletion <= substitution:
                    dp[i][j] = deletion
                    edits[i][j] = edits[i-1][j] + 'D'
                elif insertion <= deletion and insertion <= substitution:
                    dp[i][j] = insertion
                    edits[i][j] = edits[i][j-1] + 'I'
                else:
                    dp[i][j] = substitution
                    edits[i][j] = edits[i-1][j-1] + 'S'

    return dp[m][n], edits[m][n]