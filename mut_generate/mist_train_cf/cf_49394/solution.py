"""
QUESTION:
Create a function `max_ascending_subsequence(seq1, seq2)` that takes two sequences of integers as arguments and returns the longest common ascending subsequence. The function should be able to handle any two sequences of integers, and the output should be a list of integers.
"""

def max_ascending_subsequence(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    dp_table = [[[] for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if seq1[i] == seq2[j]:
                if (not dp_table[i + 1][j + 1] or dp_table[i + 1][j + 1][0] <= seq1[i]) and (not dp_table[i][j] or dp_table[i][j][0] > seq1[i]):
                    dp_table[i][j] = [seq1[i]] + dp_table[i + 1][j + 1]
                else:
                    dp_table[i][j] = dp_table[i][j]
            else:
                if dp_table[i + 1][j] and dp_table[i][j + 1]:
                    if dp_table[i + 1][j][0] >= dp_table[i][j + 1][0]:
                        dp_table[i][j] = dp_table[i + 1][j]
                    else:
                        dp_table[i][j] = dp_table[i][j + 1]
                elif dp_table[i + 1][j]:
                    dp_table[i][j] = dp_table[i + 1][j]
                else:
                    dp_table[i][j] = dp_table[i][j + 1]

    return dp_table[0][0]