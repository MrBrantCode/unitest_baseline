"""
QUESTION:
You are given a string $s$. You can build new string $p$ from $s$ using the following operation no more than two times:   choose any subsequence $s_{i_1}, s_{i_2}, \dots, s_{i_k}$ where $1 \le i_1 < i_2 < \dots < i_k \le |s|$;  erase the chosen subsequence from $s$ ($s$ can become empty);  concatenate chosen subsequence to the right of the string $p$ (in other words, $p = p + s_{i_1}s_{i_2}\dots s_{i_k}$). 

Of course, initially the string $p$ is empty. 

For example, let $s = \text{ababcd}$. At first, let's choose subsequence $s_1 s_4 s_5 = \text{abc}$ — we will get $s = \text{bad}$ and $p = \text{abc}$. At second, let's choose $s_1 s_2 = \text{ba}$ — we will get $s = \text{d}$ and $p = \text{abcba}$. So we can build $\text{abcba}$ from $\text{ababcd}$.

Can you build a given string $t$ using the algorithm above?


-----Input-----

The first line contains the single integer $T$ ($1 \le T \le 100$) — the number of test cases.

Next $2T$ lines contain test cases — two per test case. The first line contains string $s$ consisting of lowercase Latin letters ($1 \le |s| \le 400$) — the initial string.

The second line contains string $t$ consisting of lowercase Latin letters ($1 \le |t| \le |s|$) — the string you'd like to build.

It's guaranteed that the total length of strings $s$ doesn't exceed $400$.


-----Output-----

Print $T$ answers — one per test case. Print YES (case insensitive) if it's possible to build $t$ and NO (case insensitive) otherwise.


-----Example-----
Input
4
ababcd
abcba
a
b
defi
fed
xyz
x

Output
YES
NO
NO
YES
"""

def can_build_string(s: str, t: str) -> str:
    def can_build_subsequence(s, t):
        j = 0
        ptr = 0
        while j < len(s) and ptr < len(t):
            if s[j] == t[ptr]:
                ptr += 1
            j += 1
        return ptr == len(t)

    if can_build_subsequence(s, t):
        return "YES"

    pos = [0] * 26
    for char in s:
        pos[ord(char) - 97] += 1

    for i in range(len(t)):
        h = pos[:]
        if not can_build_subsequence(s, t[:i+1]):
            continue
        if can_build_subsequence(s, t[i+1:]):
            return "YES"

    return "NO"