"""
QUESTION:
Ori and Sein have overcome many difficult challenges. They finally lit the Shrouded Lantern and found Gumon Seal, the key to the Forlorn Ruins. When they tried to open the door to the ruins... nothing happened.

Ori was very surprised, but Sein gave the explanation quickly: clever Gumon decided to make an additional defence for the door.

There are $n$ lamps with Spirit Tree's light. Sein knows the time of turning on and off for the $i$-th lamp — $l_i$ and $r_i$ respectively. To open the door you have to choose $k$ lamps in such a way that there will be a moment of time when they all will be turned on.

While Sein decides which of the $k$ lamps to pick, Ori is interested: how many ways there are to pick such $k$ lamps that the door will open? It may happen that Sein may be wrong and there are no such $k$ lamps. The answer might be large, so print it modulo $998\,244\,353$.


-----Input-----

First line contains two integers $n$ and $k$ ($1 \le n \le 3 \cdot 10^5$, $1 \le k \le n$) — total number of lamps and the number of lamps that must be turned on simultaneously.

Next $n$ lines contain two integers $l_i$ ans $r_i$ ($1 \le l_i \le r_i \le 10^9$) — period of time when $i$-th lamp is turned on.


-----Output-----

Print one integer — the answer to the task modulo $998\,244\,353$.


-----Examples-----
Input
7 3
1 7
3 8
4 5
6 7
1 3
5 10
8 9

Output
9
Input
3 1
1 1
2 2
3 3

Output
3
Input
3 2
1 1
2 2
3 3

Output
0
Input
3 3
1 3
2 3
3 3

Output
1
Input
5 2
1 3
2 4
3 5
4 6
5 7

Output
7


-----Note-----

In first test case there are nine sets of $k$ lamps: $(1, 2, 3)$, $(1, 2, 4)$, $(1, 2, 5)$, $(1, 2, 6)$, $(1, 3, 6)$, $(1, 4, 6)$, $(2, 3, 6)$, $(2, 4, 6)$, $(2, 6, 7)$.

In second test case $k=1$, so the answer is 3.

In third test case there are no such pairs of lamps.

In forth test case all lamps are turned on in a time $3$, so the answer is 1.

In fifth test case there are seven sets of $k$ lamps: $(1, 2)$, $(1, 3)$, $(2, 3)$, $(2, 4)$, $(3, 4)$, $(3, 5)$, $(4, 5)$.
"""

def count_ways_to_open_door(n, k, lamps):
    MOD = 998244353
    
    # Precompute factorials and inverse factorials
    fact = [1] * (n + 1)
    rfact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    rfact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        rfact[i - 1] = rfact[i] * i % MOD

    def perm(n, k):
        return fact[n] * rfact[n - k] % MOD

    def comb(n, k):
        return fact[n] * rfact[k] * rfact[n - k] % MOD

    # Extract start and end times
    L = [lamp[0] for lamp in lamps]
    R = [lamp[1] for lamp in lamps]

    # Compress time intervals
    compLR = {e: i + 1 for (i, e) in enumerate(sorted(set(L + R)))}
    for i in range(n):
        L[i] = compLR[L[i]]
        R[i] = compLR[R[i]]

    # Initialize on and off arrays
    on = [0] * (n * 2 + 1)
    off = [0] * (n * 2 + 2)
    for (l, r) in zip(L, R):
        on[l] += 1
        off[r + 1] += 1

    # Calculate the number of ways
    ans = 0
    cum = 0
    for i in range(1, n * 2 + 1):
        cum -= off[i]
        for j in range(1, on[i] + 1):
            old = k - j
            if 0 <= old <= cum:
                ans += comb(cum, old) * comb(on[i], j) % MOD
            ans %= MOD
        cum += on[i]

    return ans