"""
QUESTION:
Chef likes to solve difficult tasks. This time, he tried to solve the Big Famous Unsolvable $A+B=C$. One of his friends played a prank on Chef and randomly shuffled the bits in $A$ and $B$ (independently in each number). However, the funny thing is that the sum of the resulting numbers remained $C$ even after shuffling.
Chef is now wondering: in how many ways is it possible to shuffle the bits of $A$ and the bits of $B$ such that their sum after shuffling is equal to $C$? Let's denote the integers obtained by shuffling the bits of $A$ and $B$ by $A_s$ and $B_s$ respectively; two ways $(A_{s1}, B_{s1})$ and $(A_{s2}, B_{s2})$ are considered distinct if $A_{s1} \neq A_{s2}$ or $B_{s1} \neq B_{s2}$.
It is allowed to add any number (possibly zero) of leading zeroes, i.e. bits $0$, to $A$ and any number of leading zeroes to $B$ before shuffling the bits.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $A$, $B$ and $C$. 

-----Output-----
For each test case, print a single line containing one integer — the number of ways to shuffle the bits.

-----Constraints-----
- $1 \le T \le 1,000$
- $1 \le A, B, C \le 10^9$
- $A+B = C$

-----Subtasks-----
Subtask #1 (50 points): $1 \le A, B, C \le 10^5$
Subtask #2 (50 points): original constraints

-----Example Input-----
2
1 2 3
369 428 797

-----Example Output-----
2
56

-----Explanation-----
Example case 1: We can consider $A=01$ and $B=10$ in binary. Then, there are two possible ways: swapping the two bits of $A$ and the two bits of $B$ ($A_s=10$, $B_s=01$ in binary, $2$ and $1$ in decimal representation) or not shuffling any bits.
"""

import math

def csb(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

def f(ca, cb, i, cf, C, n, dp):
    if ca < 0 or cb < 0:
        return 0
    if i == n:
        if ca == 0 and cb == 0 and (cf == 0):
            return 1
        return 0
    st = str(ca) + ' ' + str(cb) + ' ' + str(cf) + ' ' + str(i)
    if dp.get(st) != None:
        return dp[st]
    x = 0
    if C & 1 << i > 0:
        x = 1
    if x == 1:
        if cf == 1:
            dp[st] = f(ca, cb, i + 1, 0, C, n, dp) + f(ca - 1, cb - 1, i + 1, 1, C, n, dp)
        else:
            dp[st] = f(ca - 1, cb, i + 1, 0, C, n, dp) + f(ca, cb - 1, i + 1, 0, C, n, dp)
    elif cf == 1:
        dp[st] = f(ca - 1, cb, i + 1, 1, C, n, dp) + f(ca, cb - 1, i + 1, 1, C, n, dp)
    else:
        dp[st] = f(ca, cb, i + 1, 0, C, n, dp) + f(ca - 1, cb - 1, i + 1, 1, C, n, dp)
    return dp[st]

def count_bit_shuffle_ways(A, B, C):
    n = int(math.log(C, 2)) + 1
    dp = {}
    return f(csb(A), csb(B), 0, 0, C, n, dp)