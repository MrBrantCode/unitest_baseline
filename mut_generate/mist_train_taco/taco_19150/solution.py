"""
QUESTION:
This is the hard version of this problem. The only difference between the easy and hard versions is the constraints on $k$ and $m$. In this version of the problem, you need to output the answer by modulo $10^9+7$.

You are given a sequence $a$ of length $n$ consisting of integers from $1$ to $n$. The sequence may contain duplicates (i.e. some elements can be equal).

Find the number of tuples of $m$ elements such that the maximum number in the tuple differs from the minimum by no more than $k$. Formally, you need to find the number of tuples of $m$ indices $i_1 < i_2 < \ldots < i_m$, such that

$$\max(a_{i_1}, a_{i_2}, \ldots, a_{i_m}) - \min(a_{i_1}, a_{i_2}, \ldots, a_{i_m}) \le k.$$

For example, if $n=4$, $m=3$, $k=2$, $a=[1,2,4,3]$, then there are two such triples ($i=1, j=2, z=4$ and $i=2, j=3, z=4$). If $n=4$, $m=2$, $k=1$, $a=[1,1,1,1]$, then all six possible pairs are suitable.

As the result can be very large, you should print the value modulo $10^9 + 7$ (the remainder when divided by $10^9 + 7$).


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 2 \cdot 10^5$) — the number of test cases. Then $t$ test cases follow.

The first line of each test case contains three integers $n$, $m$, $k$ ($1 \le n \le 2 \cdot 10^5$, $1 \le m \le 100$, $1 \le k \le n$) — the length of the sequence $a$, number of elements in the tuples and the maximum difference of elements in the tuple.

The next line contains $n$ integers $a_1, a_2,\ldots, a_n$ ($1 \le a_i \le n$) — the sequence $a$.

It is guaranteed that the sum of $n$ for all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

Output $t$ answers to the given test cases. Each answer is the required number of tuples of $m$ elements modulo $10^9 + 7$, such that the maximum value in the tuple differs from the minimum by no more than $k$.


-----Examples-----

Input
4
4 3 2
1 2 4 3
4 2 1
1 1 1 1
1 1 1
1
10 4 3
5 6 1 3 2 9 8 1 2 4
Output
2
6
1
20


-----Note-----

None
"""

MOD = 10 ** 9 + 7
N = 200001
fact = [1]
for i in range(1, N + 1):
    fact.append(fact[-1] * i % MOD)

def nCr(n, r):
    if n <= r:
        return n == r
    a = fact[n]
    b = fact[n - r] * fact[r] % MOD
    b = pow(b, MOD - 2, MOD)
    return a * b % MOD

def count_valid_tuples(n, m, k, sequence):
    if sequence.count(sequence[0]) == len(sequence):
        return math.comb(len(sequence), m) % MOD
    
    sequence.sort()
    ans = 0
    for j in range(n - m + 1):
        last = bisect.bisect_right(sequence, sequence[j] + k)
        ans += nCr(last - j - 1, m - 1)
    
    return ans % MOD