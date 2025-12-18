"""
QUESTION:
Bob decided to take a break from calculus homework and designed a game for himself.

The game is played on a sequence of piles of stones, which can be described with a sequence of integers $s_1, \ldots, s_k$, where $s_i$ is the number of stones in the $i$-th pile. On each turn, Bob picks a pair of non-empty adjacent piles $i$ and $i+1$ and takes one stone from each. If a pile becomes empty, its adjacent piles do not become adjacent. The game ends when Bob can't make turns anymore. Bob considers himself a winner if at the end all piles are empty.

We consider a sequence of piles winning if Bob can start with it and win with some sequence of moves.

You are given a sequence $a_1, \ldots, a_n$, count the number of subsegments of $a$ that describe a winning sequence of piles. In other words find the number of segments $[l, r]$ ($1 \leq l \leq r \leq n$), such that the sequence $a_l, a_{l+1}, \ldots, a_r$ is winning.


-----Input-----

Each test consists of multiple test cases. The first line contains a single integer $t$ ($1 \leq t \leq 3 \cdot 10^5$) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer $n$ ($1 \leq n \leq 3 \cdot 10^5$).

The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ ($0 \leq a_i \leq 10^9$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $3 \cdot 10^5$.


-----Output-----

Print a single integer for each test case — the answer to the problem.


-----Examples-----

Input
6
2
2 2
3
1 2 3
4
1 1 1 1
4
1 2 2 1
4
1 2 1 2
8
1 2 1 2 1 2 1 2
Output
1
0
4
2
1
3


-----Note-----

In the first test case, Bob can't win on subsegments of length $1$, as there is no pair of adjacent piles in an array of length $1$.

In the second test case, every subsegment is not winning.

In the fourth test case, the subsegment $[1, 4]$ is winning, because Bob can make moves with pairs of adjacent piles: $(2, 3)$, $(1, 2)$, $(3, 4)$. Another winning subsegment is $[2, 3]$.
"""

from collections import deque

def process(a, n):
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = a[i] - b[i - 1]
    return b

def check(a, b, n):
    c = deque([])
    c.append([0, 1])
    d = deque([])
    count = 0
    for i in range(n):
        if i % 2 == 0:
            while c and c[-1][0] > b[i]:
                c.pop()
            if c and c[-1][0] == b[i]:
                count += c[-1][1]
                c[-1][1] += 1
            else:
                c.append([b[i], 1])
            while d and b[i] < -d[0][0]:
                d.popleft()
            if d and b[i] == -d[0][0]:
                count += d[0][1]
        else:
            while c and b[i] < -c[0][0]:
                c.popleft()
            if c and b[i] == -c[0][0]:
                count += c[0][1]
            while d and d[-1][0] > b[i]:
                d.pop()
            if d and d[-1][0] == b[i]:
                count += d[-1][1]
                d[-1][1] += 1
            else:
                d.append([b[i], 1])
    return count

def count_winning_subsegments(a, n):
    b = process(a, n)
    return check(a, b, n)