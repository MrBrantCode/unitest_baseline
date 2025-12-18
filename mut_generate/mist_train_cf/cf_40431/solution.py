"""
QUESTION:
Write a function `calculate_score(mat, d, n, m, p)` that calculates the score for aligning two sequences represented by the 3D matrix `mat` using the given dictionary `d`. The function should return the total score for aligning the sequences based on the provided scoring rules.

`mat` is a 3D matrix of dimensions `n x m x p` representing the sequences to be aligned, `d` is a dictionary containing the scoring rules with keys 's', 'yz', 'y', and 'z', `n`, `m`, and `p` are integers representing the lengths of the sequences. The function should return the total score for aligning the sequences. The scores in `mat` are used as the base score, and the scores in `d` are added based on the alignment scenarios.
"""

def calculate_score(mat, d, n, m, p):
    score = 0
    for i in range(n):
        for j in range(m):
            for k in range(p):
                if i > 0 and j > 0 and k > 0:
                    score += max(mat[i][j][k] + d['s'], mat[i-1][j-1][k-1] + d['yz'], mat[i-1][j][k] + d['y'], mat[i][j-1][k] + d['z'])
                elif i == 0 and j > 0 and k > 0:
                    score += mat[i][j][k] + d['z']
                elif j == 0 and i > 0 and k > 0:
                    score += mat[i][j][k] + d['y']
                elif k == 0 and i > 0 and j > 0:
                    score += mat[i][j][k] + d['yz']
                else:
                    score += mat[i][j][k]
    return score