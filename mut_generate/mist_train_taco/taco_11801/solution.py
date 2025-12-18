"""
QUESTION:
You are given two strings $s$ and $t$, both of length $n$. Each character in both string is 'a', 'b' or 'c'.

In one move, you can perform one of the following actions:

choose an occurrence of "ab" in $s$ and replace it with "ba";

choose an occurrence of "bc" in $s$ and replace it with "cb".

You are allowed to perform an arbitrary amount of moves (possibly, zero). Can you change string $s$ to make it equal to string $t$?


-----Input-----

The first line contains a single integer $q$ ($1 \le q \le 10^4$) — the number of testcases.

The first line of each testcase contains a single integer $n$ ($1 \le n \le 10^5$) — the length of strings $s$ and $t$.

The second line contains string $s$ of length $n$. Each character is 'a', 'b' or 'c'.

The third line contains string $t$ of length $n$. Each character is 'a', 'b' or 'c'.

The sum of $n$ over all testcases doesn't exceed $10^5$.


-----Output-----

For each testcase, print "YES" if you can change string $s$ to make it equal to string $t$ by performing an arbitrary amount of moves (possibly, zero). Otherwise, print "NO".


-----Examples-----

Input
5
3
cab
cab
1
a
b
6
abbabc
bbaacb
10
bcaabababc
cbbababaac
2
ba
ab
Output
YES
NO
YES
YES
NO


-----Note-----

None
"""

def can_transform_strings(s: str, t: str) -> str:
    n = len(s)
    if len(t) != n:
        return "NO"
    
    idx1 = start = 0
    while idx1 < n:
        c1, c2 = s[idx1], t[idx1]
        if c1 == c2:
            idx1 += 1
            continue
        if c1 == 'c':
            return "NO"
        elif c1 == 'a':
            if c2 == 'c':
                return "NO"
            j = max(start, idx1 + 1)
            while j < n and s[j] != 'b':
                if s[j] == 'c':
                    return "NO"
                j += 1
            if j == n:
                return "NO"
            s = s[:idx1] + s[j] + s[idx1+1:j] + s[idx1] + s[j+1:]
            start = j + 1
        else:
            if c2 == 'a':
                return "NO"
            j = max(start, idx1 + 1)
            while j < n and s[j] != 'c':
                if s[j] == 'a':
                    return "NO"
                j += 1
            if j == n:
                return "NO"
            s = s[:idx1] + s[j] + s[idx1+1:j] + s[idx1] + s[j+1:]
            start = j + 1
        idx1 += 1
    
    if s[-1] != t[-1]:
        return "NO"
    
    return "YES"