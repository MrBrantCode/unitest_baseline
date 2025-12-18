"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Given three positive integers N, L and R, find the number of non-decreasing sequences of size at least 1 and at most N, such that each element of the sequence lies between L and R, both inclusive.

Print the answer modulo 10^{6}+3.

------ Input ------ 

First line of input contains T, the number of the test cases.
Each of next T lines contains three space separated integers N, L and R.

------ Output ------ 

For each test case print the answer modulo 10^{6}+3 in a single line.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$L ≤ R$

------ Subtasks ------ 

$Subtask #1 (20 points): 1 ≤ N, L, R ≤ 100
$$Subtask #2 (30 points): 1 ≤ N, L, R ≤ 10^{4}
$$Subtask #3 (50 points): 1 ≤ N, L, R ≤ 10^{9}

----- Sample Input 1 ------ 
2
1 4 5
2 4 5
----- Sample Output 1 ------ 
2
5
----- explanation 1 ------ 
test #1: [4] and [5] are the two sequences.
test #2: [4], [5], [4, 4], [4, 5] and [5, 5] are the five sequences.
"""

def count_non_decreasing_sequences(N, L, R, mod=10**6 + 3):
    cl = [1]

    def factorial2(n, mod):
        if n > len(cl):
            for i in range(len(cl), n):
                cl.append((i + 1) * cl[i - 1] % mod)
        return cl[n - 1]

    def select7(n, k, mod):
        if n > mod or k > mod:
            (n1, k1) = (n // mod, k // mod)
            (n0, k0) = (n % mod, k % mod)
            if n1 < k1 or n0 < k0:
                return 0
            return select7(n1, k1, mod) * select7(n0, k0, mod)
        if n == k or k == 0:
            return 1
        a = factorial2(n, mod)
        b = factorial2(k, mod)
        b = pow(b, mod - 2, mod)
        c = factorial2(n - k, mod)
        c = pow(c, mod - 2, mod)
        return a * b * c % mod

    def solve2(n, m, p):
        return (select7(m + n, n, p) - 1) % p

    return solve2(N, R - L + 1, mod)