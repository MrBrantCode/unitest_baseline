"""
QUESTION:
Coach Ankit is forming a team for the Annual Inter Galactic Relay Race. He has N students that train under him and he knows their strengths. The strength of a student is represented by a positive integer.

The coach has to form a team of K students. The strength of a team is defined by the strength of the weakest student in the team. Now he wants to know the sum of strengths of all the teams of size K that can be formed modulo 1000000007. Please help him.

Input
The first line contains the number of test cases T.
Each case begins with a line containing integers N and K. The next line contains N space-separated numbers which describe the strengths of the students.

Output
For test case output a single integer, the answer as described in the problem statement.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100000
1 ≤ K ≤ N
0 ≤ Strength of each student ≤ 2000000000
Strength of all the students are different.

SAMPLE INPUT
2
2 1
5 4
3 2
1 0 2

SAMPLE OUTPUT
9
1

Explanation

For first test case: 5+4=9, as team can only consist of 1 student.
For second test case: min(1,0) + min(1,2) + min(0,2) = 0+1+0 =1
"""

def calculate_team_strength_sum(n, k, strengths, M=1000000007):
    def modpow(a, x, p):
        # Calculates a^x mod p in logarithmic time.
        res = 1
        while x > 0:
            if x % 2 == 1:
                res *= a
                res %= p
            a = a * a
            a %= p
            x = x // 2
        return res

    def modInverse(a, p):
        # Calculates the modular multiplicative inverse of a mod p.
        # (assuming p is prime).
        return modpow(a, p - 2, p)

    def comp(n, r, fact, ifact, M):
        ret = (fact[n] * ifact[r]) % M
        ret *= ifact[n - r]
        ret %= M
        return ret

    def precompute(fact, ifact, N, M):
        fact[0] = 1
        for i in range(1, N):
            fact[i] = (i * fact[i - 1]) % M
        ifact[N - 1] = modpow(fact[N - 1], M - 2, M)
        j = N - 2
        while j >= 0:
            ifact[j] = ((j + 1) * ifact[j + 1]) % M
            j -= 1

    N = 100005
    fact = [0] * N
    ifact = [0] * N
    precompute(fact, ifact, N, M)

    strengths.sort()
    res = 0
    for i in range(n - k + 1):
        ncr = comp(n - i - 1, k - 1, fact, ifact, M)
        ncr = (ncr * strengths[i]) % M
        res = (res + ncr) % M
    return res