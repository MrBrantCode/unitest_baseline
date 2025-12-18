"""
QUESTION:
You are given two strings $s$ and $t$, both consisting only of lowercase Latin letters.

The substring $s[l..r]$ is the string which is obtained by taking characters $s_l, s_{l + 1}, \dots, s_r$ without changing the order.

Each of the occurrences of string $a$ in a string $b$ is a position $i$ ($1 \le i \le |b| - |a| + 1$) such that $b[i..i + |a| - 1] = a$ ($|a|$ is the length of string $a$).

You are asked $q$ queries: for the $i$-th query you are required to calculate the number of occurrences of string $t$ in a substring $s[l_i..r_i]$.


-----Input-----

The first line contains three integer numbers $n$, $m$ and $q$ ($1 \le n, m \le 10^3$, $1 \le q \le 10^5$) — the length of string $s$, the length of string $t$ and the number of queries, respectively.

The second line is a string $s$ ($|s| = n$), consisting only of lowercase Latin letters.

The third line is a string $t$ ($|t| = m$), consisting only of lowercase Latin letters.

Each of the next $q$ lines contains two integer numbers $l_i$ and $r_i$ ($1 \le l_i \le r_i \le n$) — the arguments for the $i$-th query.


-----Output-----

Print $q$ lines — the $i$-th line should contain the answer to the $i$-th query, that is the number of occurrences of string $t$ in a substring $s[l_i..r_i]$.


-----Examples-----
Input
10 3 4
codeforces
for
1 3
3 10
5 6
5 7

Output
0
1
0
1

Input
15 2 3
abacabadabacaba
ba
1 15
3 4
2 14

Output
4
0
3

Input
3 5 2
aaa
baaab
1 3
1 1

Output
0
0



-----Note-----

In the first example the queries are substrings: "cod", "deforces", "fo" and "for", respectively.
"""

def count_substring_occurrences(s: str, t: str, queries: list) -> list:
    """
    Counts the number of occurrences of substring `t` in each of the specified substrings of `s`.

    Parameters:
    - s (str): The main string.
    - t (str): The substring to search for.
    - queries (list): A list of tuples where each tuple contains the start (`l`) and end (`r`) indices for the substring queries.

    Returns:
    - list: A list of integers where each integer corresponds to the number of occurrences of `t` in the specified substring of `s`.
    """
    n = len(s)
    m = len(t)
    pos = [0] * n
    
    # Mark positions where `t` occurs in `s`
    for i in range(n):
        if i + m <= n and s[i:i + m] == t:
            pos[i] = 1
    
    # Create a prefix sum array for efficient range sum queries
    sum_pos = [0] * (n + 1)
    for i in range(n):
        sum_pos[i + 1] = sum_pos[i] + pos[i]
    
    results = []
    for (l, r) in queries:
        r = r - m + 1
        l -= 1
        if l < r:
            results.append(sum_pos[r] - sum_pos[l])
        else:
            results.append(0)
    
    return results