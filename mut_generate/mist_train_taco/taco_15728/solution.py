"""
QUESTION:
There are N children, numbered 1, 2, \ldots, N.

They have decided to share K candies among themselves. Here, for each i (1 \leq i \leq N), Child i must receive between 0 and a_i candies (inclusive). Also, no candies should be left over.

Find the number of ways for them to share candies, modulo 10^9 + 7. Here, two ways are said to be different when there exists a child who receives a different number of candies.

Constraints

* All values in input are integers.
* 1 \leq N \leq 100
* 0 \leq K \leq 10^5
* 0 \leq a_i \leq K

Input

Input is given from Standard Input in the following format:


N K
a_1 a_2 \ldots a_N


Output

Print the number of ways for the children to share candies, modulo 10^9 + 7.

Examples

Input

3 4
1 2 3


Output

5


Input

1 10
9


Output

0


Input

2 0
0 0


Output

1


Input

4 100000
100000 100000 100000 100000


Output

665683269
"""

def count_ways_to_share_candies(N, K, a):
    mod = 10 ** 9 + 7

    def comb(a, b):
        return fact[a] * inv[b] * inv[a - b] % mod

    fact = [1]
    for i in range(N + K):
        fact.append(fact[-1] * (i + 1) % mod)
    
    inv = [1] * (N + K + 1)
    inv[N + K] = pow(fact[N + K], mod - 2, mod)
    for i in range(N + K)[::-1]:
        inv[i] = inv[i + 1] * (i + 1) % mod
    
    f = [comb(i + N - 1, N - 1) for i in range(K + 1)]
    
    for i in a:
        for j in range(K - i)[::-1]:
            f[j + i + 1] -= f[j]
            f[j + i + 1] %= mod
    
    return f[K]