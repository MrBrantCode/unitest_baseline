"""
QUESTION:
You are given an integer $n$. You have to calculate the number of binary (consisting of characters 0 and/or 1) strings $s$ meeting the following constraints.

For every pair of integers $(i, j)$ such that $1 \le i \le j \le n$, an integer $a_{i,j}$ is given. It imposes the following constraint on the string $s_i s_{i+1} s_{i+2} \dots s_j$:

if $a_{i,j} = 1$, all characters in $s_i s_{i+1} s_{i+2} \dots s_j$ should be the same;

if $a_{i,j} = 2$, there should be at least two different characters in $s_i s_{i+1} s_{i+2} \dots s_j$;

if $a_{i,j} = 0$, there are no additional constraints on the string $s_i s_{i+1} s_{i+2} \dots s_j$.

Count the number of binary strings $s$ of length $n$ meeting the aforementioned constraints. Since the answer can be large, print it modulo $998244353$.


-----Input-----

The first line contains one integer $n$ ($2 \le n \le 100$).

Then $n$ lines follow. The $i$-th of them contains $n-i+1$ integers $a_{i,i}, a_{i,i+1}, a_{i,i+2}, \dots, a_{i,n}$ ($0 \le a_{i,j} \le 2$).


-----Output-----

Print one integer — the number of strings meeting the constraints, taken modulo $998244353$.


-----Examples-----

Input
3
1 0 2
1 0
1
Output
6
Input
3
1 1 2
1 0
1
Output
2
Input
3
1 2 1
1 0
1
Output
0
Input
3
2 0 2
0 1
1
Output
0


-----Note-----

In the first example, the strings meeting the constraints are 001, 010, 011, 100, 101, 110.

In the second example, the strings meeting the constraints are 001, 110.
"""

def count_valid_binary_strings(n, constraints):
    pr = [i for i in range(n)]
    for e in constraints:
        if e[0] == 2:
            return 0
    
    for i in range(n):
        for j in range(n - i):
            if constraints[i][j] == 1:
                for k in range(i + 1, i + j + 1):
                    pr[k] = pr[k - 1]
    
    d = [[0] * n for i in range(n)]
    d[0][0] = 2
    MOD = 998244353
    
    for i in range(1, n):
        ps = 0
        for j in range(i + 1):
            if constraints[j][i - j] == 2:
                ps = j + 1
        for j in range(ps, i):
            d[i][j] = d[i - 1][j]
        if pr[i] >= i:
            d[i][i] = sum(d[i - 1]) % MOD
    
    return sum(d[n - 1]) % MOD