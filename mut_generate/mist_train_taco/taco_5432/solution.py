"""
QUESTION:
You are given an array of $n$ positive integers $a_1, a_2, \ldots, a_n$. Your task is to calculate the number of arrays of $n$ positive integers $b_1, b_2, \ldots, b_n$ such that:

$1 \le b_i \le a_i$ for every $i$ ($1 \le i \le n$), and

$b_i \neq b_{i+1}$ for every $i$ ($1 \le i \le n - 1$).

The number of such arrays can be very large, so print it modulo $998\,244\,353$.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the length of the array $a$.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 10^9$).


-----Output-----

Print the answer modulo $998\,244\,353$ in a single line.


-----Examples-----

Input
3
2 2 2
Output
2
Input
2
2 3
Output
4
Input
3
1 1 1
Output
0


-----Note-----

In the first test case possible arrays are $[1, 2, 1]$ and $[2, 1, 2]$.

In the second test case possible arrays are $[1, 2]$, $[1, 3]$, $[2, 1]$ and $[2, 3]$.
"""

def count_valid_arrays(n, a):
    mod = 998244353
    stack = [(0, 0), (a[0], 1)]
    now = a[0]
    
    for v in a[1:]:
        to = -now
        now *= 1 - v
        now %= mod
        while stack[-1][0] > v:
            (r, d) = stack.pop()
            now -= (r - v) * d
            now %= mod
            to += d
        stack.append((v, to % mod))
    
    if n % 2 == 1:
        return now % mod
    else:
        return (mod - now) % mod