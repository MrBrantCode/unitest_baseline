"""
QUESTION:
Mark has just purchased a rack of $n$ lightbulbs. The state of the lightbulbs can be described with binary string $s = s_1s_2\dots s_n$, where $s_i={1}$ means that the $i$-th lightbulb is turned on, while $s_i={0}$ means that the $i$-th lightbulb is turned off.

Unfortunately, the lightbulbs are broken, and the only operation he can perform to change the state of the lightbulbs is the following:

Select an index $i$ from $2,3,\dots,n-1$ such that $s_{i-1}\ne s_{i+1}$.

Toggle $s_i$. Namely, if $s_i$ is ${0}$, set $s_i$ to ${1}$ or vice versa.

Mark wants the state of the lightbulbs to be another binary string $t$. Help Mark determine the minimum number of operations to do so.


-----Input-----

The first line of the input contains a single integer $q$ ($1\leq q\leq 10^4$) — the number of test cases.

The first line of each test case contains a single integer $n$ ($3\leq n\leq 2\cdot 10^5$) — the number of lightbulbs.

The second line of each test case contains a binary string $s$ of length $n$ — the initial state of the lightbulbs.

The third line of each test case contains a binary string $t$ of length $n$ — the final state of the lightbulbs.

It is guaranteed that the sum of $n$ across all test cases does not exceed $2\cdot 10^5$.


-----Output-----

For each test case, print a line containing the minimum number of operations Mark needs to perform to transform $s$ to $t$. If there is no such sequence of operations, print $-1$.


-----Examples-----

Input
4
4
0100
0010
4
1010
0100
5
01001
00011
6
000101
010011
Output
2
-1
-1
5


-----Note-----

In the first test case, one sequence of operations that achieves the minimum number of operations is the following.

Select $i=3$, changing ${01}{{0}}{0}$ to ${01}{{1}}{0}$.

Select $i=2$, changing ${0}{{1}}{10}$ to ${0}{{0}}{10}$.

In the second test case, there is no sequence of operations because one cannot change the first digit or the last digit of $s$.

In the third test case, even though the first digits of $s$ and $t$ are the same and the last digits of $s$ and $t$ are the same, it can be shown that there is no sequence of operations that satisfies the condition.

In the fourth test case, one sequence that achieves the minimum number of operations is the following:

Select $i=3$, changing ${00}{{0}}{101}$ to ${00}{{1}}{101}$.

Select $i=2$, changing ${0}{{0}}{1101}$ to ${0}{{1}}{1101}$.

Select $i=4$, changing ${011}{{1}}{01}$ to ${011}{{0}}{01}$.

Select $i=5$, changing ${0110}{{0}}{1}$ to ${0110}{{1}}{1}$.

Select $i=3$, changing ${01}{{1}}{011}$ to ${01}{{0}}{011}$.
"""

def min_operations_to_transform(s: str, t: str, n: int) -> int:
    if s[0] != t[0] or s[n - 1] != t[n - 1]:
        return -1
    
    i, j, edits = 0, 0, 0
    
    while True:
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
        while j < n - 1 and t[j] == t[j + 1]:
            j += 1
        
        if i < n - 1 and j < n - 1:
            edits += abs(i - j)
        elif i == n - 1 and j == n - 1:
            return edits + abs(i - j)
        else:
            return -1
        
        i += 1
        j += 1