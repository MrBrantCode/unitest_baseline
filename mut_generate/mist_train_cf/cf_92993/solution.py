"""
QUESTION:
Write a function `min_operations(string1, string2)` that calculates the minimum number of operations (insertions, deletions, or replacements) required to transform `string1` into `string2`, where both strings are composed of lowercase letters. Each operation has a cost of 1.
"""

def min_operations(string1, string2):
    m = len(string1)
    n = len(string2)

    # Step 1
    matrix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    # Step 2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,  # Deletion
                    matrix[i][j - 1] + 1,  # Insertion
                    matrix[i - 1][j - 1] + 1  # Replacement
                )

    # Step 3
    return matrix[m][n]