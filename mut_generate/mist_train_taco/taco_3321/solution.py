"""
QUESTION:
Memory and his friend Lexa are competing to get higher score in one popular computer game. Memory starts with score a and Lexa starts with score b. In a single turn, both Memory and Lexa get some integer in the range [ - k;k] (i.e. one integer among  - k,  - k + 1,  - k + 2, ...,  - 2,  - 1, 0, 1, 2, ..., k - 1, k) and add them to their current scores. The game has exactly t turns. Memory and Lexa, however, are not good at this game, so they both always get a random integer at their turn.

Memory wonders how many possible games exist such that he ends with a strictly higher score than Lexa. Two games are considered to be different if in at least one turn at least one player gets different score. There are (2k + 1)^2t games in total. Since the answer can be very large, you should print it modulo 10^9 + 7. Please solve this problem for Memory.


-----Input-----

The first and only line of input contains the four integers a, b, k, and t (1 ≤ a, b ≤ 100, 1 ≤ k ≤ 1000, 1 ≤ t ≤ 100) — the amount Memory and Lexa start with, the number k, and the number of turns respectively.


-----Output-----

Print the number of possible games satisfying the conditions modulo 1 000 000 007 (10^9 + 7) in one line.


-----Examples-----
Input
1 2 2 1

Output
6

Input
1 1 1 2

Output
31

Input
2 12 3 1

Output
0



-----Note-----

In the first sample test, Memory starts with 1 and Lexa starts with 2. If Lexa picks  - 2, Memory can pick 0, 1, or 2 to win. If Lexa picks  - 1, Memory can pick 1 or 2 to win. If Lexa picks 0, Memory can pick 2 to win. If Lexa picks 1 or 2, Memory cannot win. Thus, there are 3 + 2 + 1 = 6 possible games in which Memory wins.
"""

def count_winning_games(a: int, b: int, k: int, t: int) -> int:
    mod = 10 ** 9 + 7
    f = [0] * 500000

    def POW(a, b):
        if b == 0:
            return 1
        if b & 1:
            return POW(a, b // 2) ** 2 * a % mod
        else:
            return POW(a, b // 2) ** 2

    def C(n, m):
        if m > n:
            return 0
        t = f[n] * POW(f[m], mod - 2) % mod * POW(f[n - m], mod - 2) % mod
        return t

    f[0] = 1
    for i in range(1, 500000):
        f[i] = f[i - 1] * i % mod

    ans = 0
    for i in range(0, 2 * t + 1):
        t1 = POW(-1, i) * C(2 * t, i) % mod
        t2 = (C(210000 + 2 * k * t - a + b + 2 * t - 1 - (2 * k + 1) * i + 1, 2 * t) - C(1 + 2 * k * t - a + b + 2 * t - 1 - (2 * k + 1) * i, 2 * t)) % mod
        ans = (ans + t1 * t2) % mod

    return ans