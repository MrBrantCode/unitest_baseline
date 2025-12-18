"""
QUESTION:
Link to Russian translation of problem

There are N ants staying at the vertices of the N-regular polygon (one ant at one vertex). At some moment of time all the ants choose one of the edges their vertex is adjacent to and start walking along this edge. If two ants meet at some point of the edge they die. Please find the probability that all the ants will survive.

Input
The first line contains one integer T - number of test cases. The following T lines contain one integer each - N.

Output
We can consider answer as a fraction P / Q. For each test case output P * Q^-1 modulo 10^9 + 7.

Constraints
T ≤ 1000
3 ≤ N ≤ 10^11

SAMPLE INPUT
1
3

SAMPLE OUTPUT
250000002
"""

def calculate_survival_probability(T, N):
    mod = 10**9 + 7
    
    def powermod4(a, b, n):
        if b == 1:
            return a % n
        r = powermod4(a, b // 2, n)
        r = r * r % n
        if b % 2 == 1:
            r = r * a % n
        return r
    
    def modInv(a):
        return powermod4(a, mod - 2, mod)
    
    results = []
    for n in N:
        results.append(modInv(pow(2, n - 1, mod)))
    
    return results