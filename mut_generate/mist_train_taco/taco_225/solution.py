"""
QUESTION:
Currently, XXOC's rap is a string consisting of zeroes, ones, and question marks. Unfortunately, haters gonna hate. They will write $x$ angry comments for every occurrence of subsequence 01 and $y$ angry comments for every occurrence of subsequence 10. You should replace all the question marks with 0 or 1 in such a way that the number of angry comments would be as small as possible.

String $b$ is a subsequence of string $a$, if it can be obtained by removing some characters from $a$. Two occurrences of a subsequence are considered distinct if sets of positions of remaining characters are distinct.


-----Input-----

The first line contains string $s$ — XXOC's rap ($1 \le |s| \leq 10^5$). The second line contains two integers $x$ and $y$ — the number of angry comments XXOC will recieve for every occurrence of 01 and 10 accordingly ($0 \leq x, y \leq 10^6$).


-----Output-----

Output a single integer — the minimum number of angry comments.


-----Examples-----

Input
0?1
2 3
Output
4
Input
?????
13 37
Output
0
Input
?10?
239 7
Output
28
Input
01101001
5 7
Output
96


-----Note-----

In the first example one of the optimum ways to replace is 001. Then there will be $2$ subsequences 01 and $0$ subsequences 10. Total number of angry comments will be equal to $2 \cdot 2 + 0 \cdot 3 = 4$.

In the second example one of the optimum ways to replace is 11111. Then there will be $0$ subsequences 01 and $0$ subsequences 10. Total number of angry comments will be equal to $0 \cdot 13 + 0 \cdot 37 = 0$.

In the third example one of the optimum ways to replace is 1100. Then there will be $0$ subsequences 01 and $4$ subsequences 10. Total number of angry comments will be equal to $0 \cdot 239 + 4 \cdot 7 = 28$.

In the fourth example one of the optimum ways to replace is 01101001. Then there will be $8$ subsequences 01 and $8$ subsequences 10. Total number of angry comments will be equal to $8 \cdot 5 + 8 \cdot 7 = 96$.
"""

def minimize_angry_comments(s, x, y):
    c0 = 0
    c1 = 0
    r = 0
    for i in s:
        if i == '0':
            c0 += 1
        else:
            r += c0 * x
            c1 += 1
    z0 = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            z0 += 1
        else:
            r += z0 * y
    ans = r
    l0 = 0
    l1 = 0
    for i in s:
        if i == '?':
            r -= l0 * x + c0 * y
            c1 -= 1
            r += l1 * y + c1 * x
            l0 += 1
        elif i == '0':
            l0 += 1
            c0 -= 1
        else:
            l1 += 1
            c1 -= 1
        ans = min(ans, r)
    return ans