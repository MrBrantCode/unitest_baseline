"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 
Little Elephant from Zoo of Lviv likes to watch movies.
There are N different movies (numbered from 0 to N − 1) he wants to watch in some order. Of course, he will watch each movie exactly once. The priority of i^{th} movie is P_{i}.
A watching of a movie is called exciting if and only if one of the following two conditions holds:

This is the first watching.
The priority of this movie is strictly greater than the maximal priority of the movies watched so far.

Let us call the number of exciting watchings the excitingness of the order.
Help him to find the number of different watching orders whose excitingness does not exceed K. Since the answer can be large, print it modulo 1000000007 (10^{9}+7).

------ Input ------ 

The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow.
The first line of each test case contains two space-separated integers N and K. The next line contains N space-separated integers P_{1}, P_{2}, ..., P_{N}.

------ Output ------ 

For each test case, print the number of different watching orders having at most K excitingness modulo 1000000007 (10^{9}+7).

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ K ≤ N ≤ 200$
$1 ≤ P_{i} ≤ 200$

------ Example ------ 

Input:
2
3 1
3 1 2
4 3
1 2 2 3

Output:
2
24

------ Explanation ------ 

In the first case, there are two boring watching orders whose excitingness not greater than K=1: [3, 1, 2], [3, 2, 1]. Both watching orders have one exciting watching: the first watching.
In the second case, every watching order has at most 3 excitingness.
"""

from collections import Counter

mod = 10 ** 9 + 7
f = [1]
for i in range(1, 2001):
    f += (f[-1] * i % mod,)
inv = [pow(i, mod - 2, mod) for i in f]
A = lambda k, n: f[n] * inv[n - k] % mod

def count_exciting_orders(N, K, P):
    cnt = Counter(P)
    dp = [0] * (K + 1)
    values = sorted(cnt, reverse=True)
    dp[1] = f[cnt[values[0]]]
    size = cnt[values[0]]
    for i in range(1, len(values)):
        size += cnt[values[i]]
        new = [0] * (K + 1)
        for k in range(1, K + 1):
            new[k] += dp[k] * A(cnt[values[i]], size - 1)
            new[k] %= mod
            if k + 1 <= K:
                new[k + 1] += cnt[values[i]] * A(cnt[values[i]] - 1, size - 1) * dp[k]
                new[k + 1] %= mod
        dp = new
    return sum(dp[1:]) % mod