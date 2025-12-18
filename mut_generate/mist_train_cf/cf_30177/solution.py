"""
QUESTION:
Implement the function `levenshtein_distance` that calculates the Levenshtein distance between two input strings `s1` and `s2`, which is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other. The function should handle strings of different lengths and be case-sensitive.
"""

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    cost_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        cost_matrix[i][0] = i
    for j in range(n + 1):
        cost_matrix[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost_matrix[i][j] = cost_matrix[i - 1][j - 1]
            else:
                substitution = cost_matrix[i - 1][j - 1] + 1
                insertion = cost_matrix[i - 1][j] + 1
                deletion = cost_matrix[i][j - 1] + 1
                cost_matrix[i][j] = min(substitution, insertion, deletion)

    return cost_matrix[m][n]