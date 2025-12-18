"""
QUESTION:
Chef Dengklek will open a new restaurant in the city. The restaurant will be open for N days. He can cook M different types of dish. He would like to cook a single dish every day, such that for the entire N days, he only cook at most K distinct types of dishes.

In how many ways can he do that?

------ Input ------ 

The first line contains a single integer T, the number of test cases. T test cases follow. Each test case consists of a single line consisting of three integers N, M, K.

------ Output ------ 

For each test case, output a single line consisting the number of different ways he can cook for the entire N days, modulo 1000000007.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 1000$
$1 ≤ M ≤ 1000000$
$1 ≤ K ≤ 1000$

----- Sample Input 1 ------ 
4
1 1 1
2 2 2
4 3 2
5 7 3
----- Sample Output 1 ------ 
1
4
45
5887
"""

MOD = 1000000007

def fill_nks(N, mod):
    nd = [[0 for j in range(N + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        nd[i][0] = 1
        nd[i][1] = 1
    for n in range(1, N + 1):
        for k in range(2, n + 1):
            nd[n][k] = (nd[n - 1][k - 1] + k * nd[n - 1][k]) % mod
    return nd

KS = fill_nks(1000, MOD)

def dishes_exact_k(n, mpk, k, mod):
    return mpk * KS[n][k] % mod

def calculate_cooking_ways(N, M, K, MOD=1000000007):
    K = min(N, M, K)
    res = 0
    mk = 1
    for i in range(1, K + 1):
        mk = mk * (M - i + 1) % MOD
        kdishes = dishes_exact_k(N, mk, i, MOD)
        res = (res + kdishes) % MOD
    return res