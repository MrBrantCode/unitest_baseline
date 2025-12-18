"""
QUESTION:
Write a Python function named `longest_increasing_common_subsequence` that takes two sequences of integers `seq1` and `seq2` as input and returns the length of the longest increasing subsequence common to both. The function should use dynamic programming approach and return the length of the longest increasing subsequence, not the actual subsequence.
"""

def longest_increasing_common_subsequence(seq1, seq2):
    """
    This function takes two sequences of integers as input and returns the length of the longest increasing subsequence common to both.

    Parameters:
    seq1 (list): The first sequence of integers.
    seq2 (list): The second sequence of integers.

    Returns:
    int: The length of the longest increasing subsequence common to both sequences.
    """

    # Compute Longest Increasing Subsequence for both sequences
    def longest_increasing_subsequence(sequence):
        length = len(sequence)
        lis = [1] * length
        for i in range (1 , length):
            for j in range(0 , i):
                if sequence[i] > sequence[j] and lis[i] < lis[j]+1 :
                    lis[i] = lis[j]+1
        maximum = 0
        for i in range(len(lis)):
            maximum = max(maximum , lis[i])
        return maximum

    # Compute Longest Common Subsequence of two sequences
    def longest_common_subsequence(a, b):
        m = len(a)
        n = len(b)
        L = [[0 for x in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0 :
                    L[i][j] = 0
                elif a[i-1] == b[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[m][n]

    # Compute Longest Increasing Subsequence for both sequences
    lis1 = longest_increasing_subsequence(seq1)
    lis2 = longest_increasing_subsequence(seq2)

    # Compute LIS for both sequences and pick the maximum one
    lis = max(lis1, lis2)

    # Compute Longest Common Subsequence of the LIS' of both sequences
    lcs = longest_common_subsequence(seq1, seq2)

    # Return the length of the longest increasing subsequence common to both sequences
    return lcs