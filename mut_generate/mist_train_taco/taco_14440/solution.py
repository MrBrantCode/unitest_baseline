"""
QUESTION:
Takahashi is a magician. He can cast a spell on an integer sequence (a_1,a_2,...,a_M) with M terms, to turn it into another sequence (s_1,s_2,...,s_M), where s_i is the sum of the first i terms in the original sequence.

One day, he received N integer sequences, each with M terms, and named those sequences A_1,A_2,...,A_N. He will try to cast the spell on those sequences so that A_1 < A_2 < ... < A_N will hold, where sequences are compared lexicographically. Let the action of casting the spell on a selected sequence be one cast of the spell. Find the minimum number of casts of the spell he needs to perform in order to achieve his objective.

Here, for two sequences a = (a_1,a_2,...,a_M), b = (b_1,b_2,...,b_M) with M terms each, a < b holds lexicographically if and only if there exists i (1 ≦ i ≦ M) such that a_j = b_j (1 ≦ j < i) and a_i < b_i.

Constraints

* 1 ≦ N ≦ 10^3
* 1 ≦ M ≦ 10^3
* Let the j-th term in A_i be A_{(i,j)}, then 1 ≦ A_{(i,j)} ≦ 10^9.

Input

The input is given from Standard Input in the following format:


N M
A_{(1,1)} A_{(1,2)} … A_{(1,M)}
A_{(2,1)} A_{(2,2)} … A_{(2,M)}
:
A_{(N,1)} A_{(N,2)} … A_{(N,M)}


Output

Print the minimum number of casts of the spell Takahashi needs to perform. If he cannot achieve his objective, print `-1` instead.

Examples

Input

3 3
2 3 1
2 1 2
2 6 3


Output

1


Input

3 3
3 2 10
10 5 4
9 1 9


Output

-1


Input

5 5
2 6 5 6 9
2 6 4 9 10
2 6 8 6 7
2 1 7 3 8
2 1 4 8 3


Output

11
"""

from math import log2
from itertools import accumulate

def minimum_spell_casts(N, M, A):
    B = max((max(Ai) for Ai in A))
    if M == 1:
        if N == 1 or all((A[i][0] < A[i + 1][0] for i in range(N - 1))):
            return 0
        else:
            return -1
    
    logB = log2(B)
    logBi = int(logB)
    INF = 10 ** 18
    INFL = [INF] * (M - logBi - 2)

    def gen(P, t, L=min(logBi + 2, M)):
        if t <= logB:
            for k in range(t):
                P[:] = accumulate(P)
        else:
            V = [1] * L
            for k in range(1, L):
                V[k] = V[k - 1] * (t + k - 1) // k
            for i in range(L - 1, 0, -1):
                P[i] += sum((P[j] * V[i - j] for j in range(i)))
            if logBi + 2 < M:
                P[logBi + 2:] = INFL

    T = [0] * N
    ans = 0
    P = [0] * M
    for i in range(N - 1):
        (a0, a1) = A[i][:2]
        (b0, b1) = A[i + 1][:2]
        if a0 < b0:
            continue
        if a0 > b0:
            return -1
        t0 = T[i]
        v = max(t0 * a0 + a1 - b1, 0)
        if v % b0 > 0:
            T[i + 1] = t1 = (v + b0 - 1) // b0
            ans += t1
            continue
        t1 = v // b0
        if t0 <= t1:
            P[:] = A[i + 1]
            gen(P, t1 - t0)
            if P <= A[i]:
                t1 += 1
        else:
            P[:] = A[i]
            gen(P, t0 - t1)
            if A[i + 1] <= P:
                t1 += 1
        T[i + 1] = t1
        ans += t1
    
    return ans