"""
QUESTION:
A permutation of length n is an array containing each integer from 1 to n exactly once. For example, q = [4, 5, 1, 2, 3] is a permutation. For the permutation q the square of permutation is the permutation p that p[i] = q[q[i]] for each i = 1... n. For example, the square of q = [4, 5, 1, 2, 3] is p = q^2 = [2, 3, 4, 5, 1].

This problem is about the inverse operation: given the permutation p you task is to find such permutation q that q^2 = p. If there are several such q find any of them.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^6) — the number of elements in permutation p.

The second line contains n distinct integers p_1, p_2, ..., p_{n} (1 ≤ p_{i} ≤ n) — the elements of permutation p.


-----Output-----

If there is no permutation q such that q^2 = p print the number "-1".

If the answer exists print it. The only line should contain n different integers q_{i} (1 ≤ q_{i} ≤ n) — the elements of the permutation q. If there are several solutions print any of them.


-----Examples-----
Input
4
2 1 4 3

Output
3 4 2 1

Input
4
2 1 3 4

Output
-1

Input
5
2 3 4 5 1

Output
4 5 1 2 3
"""

def find_permutation_q(n, p):
    ans = [-1] * (n + 1)
    d = {}
    visited = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if visited[i] == 0:
            g = []
            abe = i
            while not visited[abe]:
                visited[abe] = 1
                g.append(abe)
                abe = p[abe - 1]
            if len(g) % 2:
                mid = (len(g) + 1) // 2
                for i in range(len(g)):
                    ans[g[i]] = g[(i + mid) % len(g)]
            elif d.get(len(g)):
                temp = d[len(g)]
                for i in range(len(g)):
                    ans[g[i]] = temp[(i + 1) % len(g)]
                    ans[temp[i]] = g[i]
                del d[len(g)]
            else:
                d[len(g)] = g
    
    if len(d):
        return -1
    
    return ans[1:]