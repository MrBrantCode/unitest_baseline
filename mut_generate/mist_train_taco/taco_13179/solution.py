"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given two binary strings $A$ and $B$, each with length $N$. You may reorder the characters of $A$ in an arbitrary way and reorder the characters of $B$ also in an arbitrary (not necessarily the same) way. Then, you should compute the XOR of the resulting strings. Find the number of distinct values of this XOR which can be obtained, modulo $1,000,000,007$ ($10^{9} + 7$).

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains a single string $A$ with length $N$.
The third line contains a single string $B$ with length $N$.

------  Output ------
For each test case, print a single line containing one integer ― the number of unique XORs modulo $1,000,000,007$.

------  Constraints  ------
$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$|A| = |B| = N$
$A$ and $B$ contain only characters '0' and '1'
the sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$

------  Subtasks ------
Subtask #1 (10 points):
$N ≤ 5$
the sum of $N$ over all test cases does not exceed $10$

Subtask #2 (30 points):
$N ≤ 1,000$
the sum of $N$ over all test cases does not exceed $2 \cdot 10^{3}$

Subtask #3 (60 points): original constraints

----- Sample Input 1 ------ 
1

2

00

10
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 
Example case 1: The characters in each string can be reordered in two ways (swap them or do nothing), so there are four values of their XOR:
- "00" XOR "10" is "10"
- "00" XOR "01" is "01"
- "00" XOR "10" is "10"
- "00" XOR "01" is "01"

There are only two distinct values.
"""

mod = 10 ** 9 + 7

def add(a, b):
    return (a % mod + b % mod) % mod

def mul(a, b):
    return a % mod * (b % mod) % mod

def ncr(n, r):
    return mul(fact[n], mul(pow(fact[n - r], mod - 2, mod), pow(fact[r], mod - 2, mod)))

def count_distinct_xor_values(n, a, b):
    ca1 = a.count('1')
    cb1 = b.count('1')
    o = abs(ca1 - cb1)
    stop = abs(min(ca1, cb1) - min(n - ca1, n - cb1))
    ans = 0
    for i in range(n - o, stop - 1, -2):
        ans = add(ans, ncr(n, i))
    return ans

# Precompute factorials up to 10^5
fact = [1]
for i in range(1, 10 ** 5 + 1):
    fact.append(mul(fact[-1], i))