"""
QUESTION:
There is a complete graph of m vertices. Initially, the edges of the complete graph are uncolored. Sunuke did the following for each i (1 ≤ i ≤ n): Select ai vertices from the complete graph and color all edges connecting the selected vertices with color i. None of the sides were painted in multiple colors. Find the minimum value that can be considered as m.

Constraints

* 1 ≤ n ≤ 5
* 2 ≤ ai ≤ 109

Input


n
a1
.. ..
an


Output

Output the minimum value of m on one line.

Examples

Input

2
3
3


Output

5


Input

5
2
3
4
5
6


Output

12
"""

def find_minimum_vertices(n, A):
    INF = 10 ** 18
    N2 = 2 ** n

    def dfs(i, D):
        if i == n:
            return sum(D)
        b = 1 << i
        a = A[i]

        def sel(j, state, u):
            if j == N2:
                D2 = D[:]
                for e in u:
                    D2[e] -= 1
                    D2[e | b] += 1
                D2[b] = a - len(u)
                return dfs(i + 1, D2)
            r = sel(j + 1, state, u)
            if D[j] > 0 and state & j == 0 and (len(u) < a):
                u.append(j)
                r = min(r, sel(j + 1, state | j, u))
                u.pop()
            return r
        return sel(0, 0, [])

    return dfs(0, [0] * N2)