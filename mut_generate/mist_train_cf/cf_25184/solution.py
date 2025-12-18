"""
QUESTION:
Implement a function `lcs` that takes two strings `X` and `Y` and their lengths `m` and `n` as input, and returns the length of the longest common subsequence between `X` and `Y`. Assume that the input strings only contain alphabetic characters and the lengths are valid.
"""

def lcs(X, Y, m, n):
    """
    This function calculates the length of the longest common subsequence between two strings X and Y.

    Parameters:
    X (str): The first input string.
    Y (str): The second input string.
    m (int): The length of the first string.
    n (int): The length of the second string.

    Returns:
    int: The length of the longest common subsequence between X and Y.
    """
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]