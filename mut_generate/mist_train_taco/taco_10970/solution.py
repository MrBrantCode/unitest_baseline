"""
QUESTION:
This is the first subtask of problem F. The only differences between this and the second subtask are the constraints on the value of $m$ and the time limit. You need to solve both subtasks in order to hack this one.

There are $n+1$ distinct colours in the universe, numbered $0$ through $n$. There is a strip of paper $m$ centimetres long initially painted with colour $0$. 

Alice took a brush and painted the strip using the following process. For each $i$ from $1$ to $n$, in this order, she picks two integers $0 \leq a_i < b_i \leq m$, such that the segment $[a_i, b_i]$ is currently painted with a single colour, and repaints it with colour $i$. 

Alice chose the segments in such a way that each centimetre is now painted in some colour other than $0$. Formally, the segment $[i-1, i]$ is painted with colour $c_i$ ($c_i \neq 0$). Every colour other than $0$ is visible on the strip.

Count the number of different pairs of sequences $\{a_i\}_{i=1}^n$, $\{b_i\}_{i=1}^n$ that result in this configuration. 

Since this number may be large, output it modulo $998244353$.


-----Input-----

The first line contains a two integers $n$, $m$ ($1 \leq n \leq 500$, $n = m$) — the number of colours excluding the colour $0$ and the length of the paper, respectively.

The second line contains $m$ space separated integers $c_1, c_2, \ldots, c_m$ ($1 \leq c_i \leq n$) — the colour visible on the segment $[i-1, i]$ after the process ends. It is guaranteed that for all $j$ between $1$ and $n$ there is an index $k$ such that $c_k = j$.

Note that since in this subtask $n = m$, this means that $c$ is a permutation of integers $1$ through $n$.


-----Output-----

Output a single integer — the number of ways Alice can perform the painting, modulo $998244353$.


-----Examples-----
Input
3 3
1 2 3

Output
5

Input
7 7
4 5 1 6 2 3 7

Output
165



-----Note-----

In the first example, there are $5$ ways, all depicted in the figure below. Here, $0$ is white, $1$ is red, $2$ is green and $3$ is blue.

[Image]

Below is an example of a painting process that is not valid, as in the second step the segment 1 3 is not single colour, and thus may not be repainted with colour $2$.

[Image]
"""

def count_painting_ways(n, m, colors):
    MOD = 998244353
    
    class SparseTable:
        def __init__(self, array, n):
            n = len(array)
            self.row_size = n.bit_length()
            self.log_table = [0] * (n + 1)
            for i in range(2, n + 1):
                self.log_table[i] = self.log_table[i // 2] + 1
            self.sparse_table = [[0] * n for _ in range(self.row_size)]
            for i in range(n):
                self.sparse_table[0][i] = array[i]
            for row in range(1, self.row_size):
                for i in range(n - (1 << row) + 1):
                    self.sparse_table[row][i] = self._merge(self.sparse_table[row - 1][i], self.sparse_table[row - 1][i + (1 << row - 1)])

        def _merge(self, num1, num2):
            return min(num1, num2)

        def query(self, l, r):
            row = self.log_table[r - l]
            return self._merge(self.sparse_table[row][l], self.sparse_table[row][r - (1 << row)])

    sp = SparseTable(colors, n)
    to_ind = {}
    for i in range(n):
        to_ind[colors[i]] = i
    dp = [[-1] * (n + 1) for i in range(n + 1)]

    def solve(l, r):
        if dp[l][r] != -1:
            return dp[l][r]
        if l == r:
            dp[l][r] = 1
            return 1
        if r - l == 1:
            dp[l][r] = 1
            return 1
        ind = to_ind[sp.query(l, r)]
        res1 = 0
        res2 = 0
        for i in range(ind + 1, r + 1):
            res1 += solve(ind + 1, i) * solve(i, r)
            res1 %= MOD
        for i in range(l, ind + 1):
            res2 += solve(l, i) * solve(i, ind)
            res2 %= MOD
        dp[l][r] = max(res1, 1) * max(res2, 1)
        dp[l][r] %= MOD
        return dp[l][r]

    return solve(0, n) % MOD