"""
QUESTION:
We have 3N cards arranged in a row from left to right, where each card has an integer between 1 and N (inclusive) written on it. The integer written on the i-th card from the left is A_i.

You will do the following operation N-1 times:

* Rearrange the five leftmost cards in any order you like, then remove the three leftmost cards. If the integers written on those three cards are all equal, you gain 1 point.



After these N-1 operations, if the integers written on the remaining three cards are all equal, you will gain 1 additional point.

Find the maximum number of points you can gain.

Constraints

* 1 \leq N \leq 2000
* 1 \leq A_i \leq N

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 \cdots A_{3N}


Output

Print the maximum number of points you can gain.

Examples

Input

2
1 2 1 2 2 1


Output

2


Input

3
1 1 2 2 3 3 3 2 1


Output

1


Input

3
1 1 2 2 2 3 3 3 1


Output

3
"""

def max_points_from_cards(N, A):
    A = A + [0] * 2  # Pad the list to handle edge cases
    X = [[-10 ** 10] * (N + 1) for _ in range(N + 1)]
    X[A[0]][A[1]] = 0
    ans = 0
    ma = 0
    MA = [-5] * (N + 1)
    MA[A[0]] = MA[A[1]] = 0
    
    for i in range(N):
        B = A[i * 3 + 2:i * 3 + 5]
        cnt = len(set(B))
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            a1 = B[0] ^ B[1] ^ B[2]
            a2 = (sum(B) - a1) // 2
            X[a1] = [max(X[a2][j] + 1, X[j][a2] + 1, MA[j]) for j in range(N + 1)]
            X[a1][a2] = max(ma, X[a2][a2] + 1)
            X[a2][a2] = max(ma, X[a1][a1] + 1)
            X[a2] = [max(x, m) for (x, m) in zip(X[a2], MA)]
            MA = [max(m, x1, x2) for (m, x1, x2) in zip(MA, X[a1], X[a2])]
            MA[a1] = max(MA[a1], max(X[a1]))
            MA[a2] = max(MA[a2], X[a1][a2], X[a2][a2])
            ma = max(ma, MA[a1], MA[a2])
        else:
            a, b, c = B
            X[a][b] = max(ma, X[c][c] + 1)
            X[a][c] = max(ma, X[b][b] + 1)
            X[b][c] = max(ma, X[a][a] + 1)
            X[a] = [max(x, m) for (x, m) in zip(X[a], MA)]
            X[b] = [max(x, m) for (x, m) in zip(X[b], MA)]
            X[c] = [max(x, m) for (x, m) in zip(X[c], MA)]
            MA[a] = max(MA[a], max(X[a]))
            MA[b] = max(MA[b], X[a][b], max(X[b]))
            MA[c] = max(MA[c], X[a][c], X[b][c], max(X[c]))
            MA = [max(m, xa, xb, xc) for (m, xa, xb, xc) in zip(MA, X[a], X[b], X[c])]
            ma = max(ma, MA[a], MA[b], MA[c])
    
    return ans + max(ma, max((max(x) for x in X)))