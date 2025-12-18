"""
QUESTION:
Implement a function `smith_waterman(seq1, seq2, match=3, mismatch=-3, gap=-2)` that performs local alignment on two DNA sequences `seq1` and `seq2` using the Smith-Waterman algorithm. The function should take four parameters: two DNA sequences `seq1` and `seq2`, and three scoring parameters: `match`, `mismatch`, and `gap`. The function should print the scoring matrix and the optimal alignment between the two sequences. The function should handle gaps in the alignment and score them according to the provided scoring schema.
"""

def smith_waterman(seq1, seq2, match=3, mismatch=-3, gap=-2):
    # Scoring matrix for Smith Waterman
    score = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    # Function to calculate the score according to the scoring schema
    def match_score(alpha, beta):
        if alpha == beta:
            return match
        elif alpha == '-' or beta == '-':
            return gap
        else:
            return mismatch

    # Calculate score for each position in the matrix
    for i in range(0, len(seq1) + 1):
        for j in range(0, len(seq2) + 1):
            if i == 0 and j == 0:
                score[i][j] = 0
            elif i == 0:
                score[i][j] = max(0, score[i][j - 1] + gap)
            elif j == 0:
                score[i][j] = max(0, score[i - 1][j] + gap)
            else:
                diag = score[i - 1][j - 1] + match_score(seq1[i - 1], seq2[j - 1])
                delete = score[i - 1][j] + gap
                insert = score[i][j - 1] + gap
                score[i][j] = max(0, diag, delete, insert)

    # Print the scoring matrix
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in score]))

    # Trace back the highest scoring path
    align1 = ""
    align2 = ""
    j = len(seq2)
    i = max(enumerate(score[-1]), key=lambda x: x[1])[0]
    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diag = score[i - 1][j - 1]
        score_left = score[i][j - 1]
        score_up = score[i - 1][j]

        if score_current == score_diag + match_score(seq1[i - 1], seq2[j - 1]):
            a1, a2 = seq1[i - 1], seq2[j - 1]
            i, j = i - 1, j - 1
        elif score_current == score_up + gap:
            a1, a2 = seq1[i - 1], '-'
            i -= 1
        elif score_current == score_left + gap:
            a1, a2 = '-', seq2[j - 1]
            j -= 1
        align1 += a1
        align2 += a2

    align1 = align1[::-1]
    align2 = align2[::-1]
    print("Optimal alignment:")
    print(align1 + "\n" + align2)