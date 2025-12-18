"""
QUESTION:
Write a function `compute_U(N)` that calculates `U(N) = ∑[R(n) from n=3 to N]`, where `R(n)` is the difference between the winning probabilities of the three cars on a circular track of length `3n`, facing the same direction, initially distance `n` apart. The cars move in turn with equal probabilities of 1, 2, 3, or 4 steps. The chase ends when the moving car reaches or goes beyond the position of the other car. The moving car is declared the winner. Return `U(N)` rounded to 8 digits after the decimal point.
"""

def compute_U(N):
    res = 0.0
    for n in range(3, N+1):
        probs = [[[0.0, 0.0, 0.0] for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(i, n+1):
                for k in range(1, 5):
                    if i <= k:
                        probs[i][j][0] += 0.25
                    else:
                        p = probs[i-k][i][:]
                        p[0], p[1] = p[1]+0.25*p[0], p[2]+0.25*p[0]
                        probs[i][j][0] += p[0]
                        probs[i][j][1] += p[1]
                        probs[i][j][2] += p[2]
                for k in range(1, 5):
                    if j <= k:
                        probs[i][j][1] += 0.25
                    else:
                        p = probs[j-k][j][:]
                        p[0], p[1], p[2] = p[2]+0.25*p[1], p[0]+0.25*p[1], p[2]+0.25*p[1]
                        probs[i][j][0] += p[0]
                        probs[i][j][1] += p[1]
                        probs[i][j][2] += p[2]
                for k in range(1, 5):
                    if i <= k:
                        probs[i][j][2] += 0.25
                    else:
                        p = probs[i-k][i][:]
                        p[0], p[2] = p[2]+0.25*p[0], p[0]+0.25*p[0]
                        probs[i][j][0] += p[0]
                        probs[i][j][1] += p[1]
                        probs[i][j][2] += p[2]
        res += max(probs[n][n]) - min(probs[n][n])
    return round(res, 8)