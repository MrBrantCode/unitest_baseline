"""
QUESTION:
You are given an integer m as a product of integers a_1, a_2, ... a_{n} $(m = \prod_{i = 1}^{n} a_{i})$. Your task is to find the number of distinct decompositions of number m into the product of n ordered positive integers.

Decomposition into n products, given in the input, must also be considered in the answer. As the answer can be very large, print it modulo 1000000007 (10^9 + 7).


-----Input-----

The first line contains positive integer n (1 ≤ n ≤ 500). The second line contains space-separated integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9).


-----Output-----

In a single line print a single number k — the number of distinct decompositions of number m into n ordered multipliers modulo 1000000007 (10^9 + 7).


-----Examples-----
Input
1
15

Output
1

Input
3
1 1 2

Output
3

Input
2
5 7

Output
4



-----Note-----

In the second sample, the get a decomposition of number 2, you need any one number out of three to equal 2, and the rest to equal 1.

In the third sample, the possible ways of decomposing into ordered multipliers are [7,5], [5,7], [1,35], [35,1].

A decomposition of positive integer m into n ordered multipliers is a cortege of positive integers b = {b_1, b_2, ... b_{n}} such that $m = \prod_{i = 1}^{n} b_{i}$. Two decompositions b and c are considered different, if there exists index i such that b_{i} ≠ c_{i}.
"""

def count_distinct_decompositions(n, A):
    Mod = 1000000007
    MAX = 33000
    B = [0] * MAX
    bePrime = [0] * MAX
    primNum = []
    C = []
    fac = [1]
    
    for j in range(1, MAX):
        fac.append(fac[-1] * j % Mod)

    def calc(M, N):
        return fac[M] * pow(fac[N] * fac[M - N] % Mod, Mod - 2, Mod) % Mod
    
    for j in range(2, MAX):
        if bePrime[j] == 0:
            primNum.append(j)
            i = j
            while i < MAX:
                bePrime[i] = 1
                i = i + j
    
    for x in A:
        tmp = x
        for j in primNum:
            while tmp % j == 0:
                tmp //= j
                B[j] += 1
        if tmp > 1:
            C.append(tmp)
    
    ans = 1
    for j in range(2, MAX):
        if B[j] > 0:
            ans = ans * calc(n + B[j] - 1, n - 1) % Mod
    
    l = len(C)
    for j in range(0, l):
        num = 0
        for k in range(0, l):
            if C[k] == C[j]:
                num = num + 1
                if k > j:
                    num = 0
                    break
        if num > 0:
            ans = ans * calc(n + num - 1, n - 1) % Mod
    
    return ans % Mod