"""
QUESTION:
The only difference between easy and hard versions is constraints.

You are given a sequence $a$ consisting of $n$ positive integers.

Let's define a three blocks palindrome as the sequence, consisting of at most two distinct elements (let these elements are $a$ and $b$, $a$ can be equal $b$) and is as follows: $[\underbrace{a, a, \dots, a}_{x}, \underbrace{b, b, \dots, b}_{y}, \underbrace{a, a, \dots, a}_{x}]$. There $x, y$ are integers greater than or equal to $0$. For example, sequences $[]$, $[2]$, $[1, 1]$, $[1, 2, 1]$, $[1, 2, 2, 1]$ and $[1, 1, 2, 1, 1]$ are three block palindromes but $[1, 2, 3, 2, 1]$, $[1, 2, 1, 2, 1]$ and $[1, 2]$ are not.

Your task is to choose the maximum by length subsequence of $a$ that is a three blocks palindrome.

You have to answer $t$ independent test cases.

Recall that the sequence $t$ is a a subsequence of the sequence $s$ if $t$ can be derived from $s$ by removing zero or more elements without changing the order of the remaining elements. For example, if $s=[1, 2, 1, 3, 1, 2, 1]$, then possible subsequences are: $[1, 1, 1, 1]$, $[3]$ and $[1, 2, 1, 3, 1, 2, 1]$, but not $[3, 2, 3]$ and $[1, 1, 1, 1, 2]$.


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 2000$) — the number of test cases. Then $t$ test cases follow.

The first line of the test case contains one integer $n$ ($1 \le n \le 2000$) — the length of $a$. The second line of the test case contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 26$), where $a_i$ is the $i$-th element of $a$. Note that the maximum value of $a_i$ can be up to $26$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2000$ ($\sum n \le 2000$).


-----Output-----

For each test case, print the answer — the maximum possible length of some subsequence of $a$ that is a three blocks palindrome.


-----Example-----
Input
6
8
1 1 2 2 3 2 1 1
3
1 3 3
4
1 10 10 1
1
26
2
2 1
3
1 1 1

Output
7
2
4
1
1
3
"""

def max_three_blocks_palindrome_length(n, a):
    M = 27
    aa = [[0] * (n + 1) for _ in range(M)]
    numind = [[] for _ in range(M)]
    
    for (i, x) in enumerate(a):
        numind[x].append(i)
        for j in range(M):
            aa[j][i + 1] = aa[j][i] + (x == j)
    
    res = 0
    for i in range(M):
        res = max(res, aa[i][-1])
    
    for a_val in range(1, M):
        for cnta in range(1, aa[a_val][-1] // 2 + 1):
            l = numind[a_val][cnta - 1]
            r = numind[a_val][aa[a_val][-1] - cnta]
            cnt = [0] * M
            for i in range(l, r + 1):
                if a[i] != a_val:
                    cnt[a[i]] += 1
            ans = cnta * 2 + max(cnt)
            res = max(res, ans)
    
    return res