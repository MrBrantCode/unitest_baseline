"""
QUESTION:
A sequence $a_1, a_2, \dots, a_k$ is called an arithmetic progression if for each $i$ from $1$ to $k$ elements satisfy the condition $a_i = a_1 + c \cdot (i - 1)$ for some fixed $c$.

For example, these five sequences are arithmetic progressions: $[5, 7, 9, 11]$, $[101]$, $[101, 100, 99]$, $[13, 97]$ and $[5, 5, 5, 5, 5]$. And these four sequences aren't arithmetic progressions: $[3, 1, 2]$, $[1, 2, 4, 8]$, $[1, -1, 1, -1]$ and $[1, 2, 3, 3, 3]$.

You are given a sequence of integers $b_1, b_2, \dots, b_n$. Find any index $j$ ($1 \le j \le n$), such that if you delete $b_j$ from the sequence, you can reorder the remaining $n-1$ elements, so that you will get an arithmetic progression. If there is no such index, output the number -1.


-----Input-----

The first line of the input contains one integer $n$ ($2 \le n \le 2\cdot10^5$) — length of the sequence $b$. The second line contains $n$ integers $b_1, b_2, \dots, b_n$ ($-10^9 \le b_i \le 10^9$) — elements of the sequence $b$.


-----Output-----

Print such index $j$ ($1 \le j \le n$), so that if you delete the $j$-th element from the sequence, you can reorder the remaining elements, so that you will get an arithmetic progression. If there are multiple solutions, you are allowed to print any of them. If there is no such index, print -1.


-----Examples-----
Input
5
2 6 8 7 4

Output
4
Input
8
1 2 3 4 5 6 7 8

Output
1
Input
4
1 2 4 8

Output
-1


-----Note-----

Note to the first example. If you delete the $4$-th element, you can get the arithmetic progression $[2, 4, 6, 8]$.

Note to the second example. The original sequence is already arithmetic progression, so you can delete $1$-st or last element and you will get an arithmetical progression again.
"""

def find_index_for_arithmetic_progression(n, b):
    def readMultiple(f):
        return f(map(int, input().split()))

    def check_seq(n, a):
        d = a[1][0] - a[0][0]
        (found, ind, prev) = (False, a[0][1], a[1][0])
        for i in range(2, n):
            if abs(a[i][0] - prev - d) > 0.1:
                if found:
                    return (False, -1)
                found = True
                ind = a[i][1]
                continue
            prev = a[i][0]
        return (True, ind)

    if n <= 3:
        return 1

    a = [(x, i + 1) for (i, x) in enumerate(b)]
    a = sorted(a)
    (is_good, ind) = check_seq(n, a)
    if not is_good:
        (is_good, ind) = check_seq(n, list(reversed(a)))
    return ind