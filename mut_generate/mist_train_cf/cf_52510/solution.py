"""
QUESTION:
Design a function named `smith_waterman_advanced` that takes two DNA sequences as input and returns their local sequence alignment. The function should implement a local sequence alignment algorithm similar to the Smith-Waterman Algorithm, with a scoring scheme that awards 1 for matches, -1 for mismatches, and -2 for gaps. The function should be able to handle sequences with varying lengths and return the aligned sequences as a tuple of two strings.
"""

import numpy as np

def smith_waterman_advanced(seq1, seq2):
    score_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1))

    # scoring scheme
    match = 1
    mismatch = -1
    gap = -2

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            score = [match if seq1[i-1] == seq2[j-1] else mismatch, 
                     gap, 
                     gap, 
                     0]
            
            from_diag = score_matrix[i-1][j-1] + score[0]
            from_top = score_matrix[i-1][j] + score[1]
            from_left = score_matrix[i][j-1] + score[2]

            score_matrix[i][j] = max(from_diag, from_top, from_left, score[3])

    max_score = np.max(score_matrix)
    max_score_index = np.where(score_matrix == max_score)

    align1 = ""
    align2 = ""

    i = max_score_index[0][0]
    j = max_score_index[1][0]

    while (i > 0 or j > 0):
        current_score = score_matrix[i][j]

        if (i > 0 and j > 0 and seq1[i-1] == seq2[j-1]):
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif (i > 0 and score_matrix[i][j] == score_matrix[i-1][j] - 2):
            align1 += seq1[i-1]
            align2 += "-"
            i -= 1
        elif (j > 0 and score_matrix[i][j] == score_matrix[i][j-1] - 2):
            align1 += "-"
            align2 += seq2[j-1]
            j -= 1
        else:
            break

    return align1[::-1], align2[::-1]