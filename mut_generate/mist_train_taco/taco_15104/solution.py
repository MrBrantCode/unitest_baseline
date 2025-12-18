"""
QUESTION:
Example

Input

2 2 7
3 4
3 2
1 3
1 1
2 2
1 2
2 1
1 2
2 2
1 1


Output

5
"""

def find_minimum_time(P, R, T, L, RS, LG):
    prv = -1
    K = [[0] * R for _ in range(P)]

    def check(t):
        nonlocal prv
        if prv < t:
            for i in range(prv + 1, t + 1):
                p, r = LG[i]
                K[p - 1][r - 1] += 1
                L[r - 1] -= 1
        else:
            for i in range(t + 1, prv + 1):
                p, r = LG[i]
                K[p - 1][r - 1] -= 1
                L[r - 1] += 1
        S = L[:]
        U = [0] * P
        updated = 1
        while updated:
            updated = 0
            for i in range(P):
                if U[i]:
                    continue
                for j in range(R):
                    if RS[i][j] - K[i][j] > max(S[j], 0):
                        break
                else:
                    U[i] = 1
                    for j in range(R):
                        S[j] += K[i][j]
                    updated = 1
        prv = t
        return sum(U) == P

    left = 0
    right = T
    while left + 1 < right:
        mid = (left + right) >> 1
        if check(mid):
            left = mid
        else:
            right = mid

    if right == T:
        return -1
    else:
        return right + 1