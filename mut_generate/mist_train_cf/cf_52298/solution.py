"""
QUESTION:
Write a function `lcsOf3(X, Y, Z, m, n, o)` that finds the length of the longest common subsequence for the given three string sequences `X`, `Y`, and `Z` of lengths `m`, `n`, and `o` respectively. The function should be able to handle special characters and numbers in the string sequences, and have a time complexity better than O(n^3), where n is the length of the longest sequence.
"""

def lcsOf3(X, Y, Z, m, n, o):
    """
    This function finds the length of the longest common subsequence for the given three string sequences X, Y, and Z of lengths m, n, and o respectively.

    Args:
        X (str): The first string sequence.
        Y (str): The second string sequence.
        Z (str): The third string sequence.
        m (int): The length of the first string sequence.
        n (int): The length of the second string sequence.
        o (int): The length of the third string sequence.

    Returns:
        int: The length of the longest common subsequence.
    """

    # Create a 3D array to store the lengths of common subsequences
    L = [[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]

    # Fill the 3D array using dynamic programming
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                elif (X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]):
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else:
                    L[i][j][k] = max(max(L[i - 1][j][k], L[i][j - 1][k]), L[i][j][k - 1])

    # Return the length of the longest common subsequence
    return L[m][n][o]