"""
QUESTION:
You are given $n$ strings $s_1, s_2, \dots, s_n$ of length at most $\mathbf{8}$.

For each string $s_i$, determine if there exist two strings $s_j$ and $s_k$ such that $s_i = s_j + s_k$. That is, $s_i$ is the concatenation of $s_j$ and $s_k$. Note that $j$ can be equal to $k$.

Recall that the concatenation of strings $s$ and $t$ is $s + t = s_1 s_2 \dots s_p t_1 t_2 \dots t_q$, where $p$ and $q$ are the lengths of strings $s$ and $t$ respectively. For example, concatenation of "code" and "forces" is "codeforces".


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases.

The first line of each test case contains a single integer $n$ ($1 \leq n \leq 10^5$) — the number of strings.

Then $n$ lines follow, the $i$-th of which contains non-empty string $s_i$ of length at most $\mathbf{8}$, consisting of lowercase English letters. Among the given $n$ strings, there may be equal (duplicates).

The sum of $n$ over all test cases doesn't exceed $10^5$.


-----Output-----

For each test case, output a binary string of length $n$. The $i$-th bit should be ${1}$ if there exist two strings $s_j$ and $s_k$ where $s_i = s_j + s_k$, and ${0}$ otherwise. Note that $j$ can be equal to $k$.


-----Examples-----

Input
3
5
abab
ab
abc
abacb
c
3
x
xx
xxx
8
codeforc
es
codes
cod
forc
forces
e
code
Output
10100
011
10100101


-----Note-----

In the first test case, we have the following:

$s_1 = s_2 + s_2$, since ${abab} = {ab} + {ab}$. Remember that $j$ can be equal to $k$.

$s_2$ is not the concatenation of any two strings in the list.

$s_3 = s_2 + s_5$, since ${abc} = {ab} + {c}$.

$s_4$ is not the concatenation of any two strings in the list.

$s_5$ is not the concatenation of any two strings in the list.

Since only $s_1$ and $s_3$ satisfy the conditions, only the first and third bits in the answer should be ${1}$, so the answer is ${10100}$.
"""

def find_concatenated_strings(test_cases):
    results = []
    
    for case in test_cases:
        n = len(case)
        strings_set = set(case)
        result = ''
        
        for s in case:
            found = False
            for k in range(1, len(s)):
                if s[k:] in strings_set and s[:k] in strings_set:
                    result += '1'
                    found = True
                    break
            if not found:
                result += '0'
        
        results.append(result)
    
    return results