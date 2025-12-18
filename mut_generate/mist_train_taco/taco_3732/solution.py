"""
QUESTION:
Chef has a strip of length $N$ units and he wants to tile it using $4$ kind of tiles

-A Red tile of $2$ unit length

-A Red tile of $1$ unit length

-A Blue tile of $2$ unit length

-A Blue tile of $1$ unit length   
Chef is having an infinite supply of each of these tiles. He wants to find out the number of ways in which he can tile the strip. Help him find this number.
Since this number can be large, output your answer modulo 1000000007 ($10^9 + 7$).

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, an integer $N$. 

-----Output:-----
For each testcase, output in a single line your answer modulo 1000000007.

-----Constraints-----
- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^{18}$

-----Sample Input:-----
1
2

-----Sample Output:-----
6

-----EXPLANATION:-----

It can be seen that for a strip of length $2$, there are $6$ possible configurations.     
$NOTE : $ 2 tiles of 1 unit length are different from 1 tile of 2 unit length.
"""

MOD = 1000000007

def count_tiling_ways(N):
    if N == 0:
        return 1
    elif N == 1:
        return 2
    elif N == 2:
        return 6
    else:
        return fib(N - 1)

def fib(n):
    F = [[2, 2], [1, 0]]
    power(F, n - 1)
    ans = [6, 2]
    return (F[0][0] * 6 + F[0][1] * 2) % MOD

def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0]) % MOD
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1]) % MOD
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0]) % MOD
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1]) % MOD
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[2, 2], [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)