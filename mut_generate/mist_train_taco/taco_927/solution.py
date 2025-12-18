"""
QUESTION:
Dreamoon has a string s and a pattern string p. He first removes exactly x characters from s obtaining string s' as a result. Then he calculates $\operatorname{occ}(s^{\prime}, p)$ that is defined as the maximal number of non-overlapping substrings equal to p that can be found in s'. He wants to make this number as big as possible.

More formally, let's define $\operatorname{ans}(x)$ as maximum value of $\operatorname{occ}(s^{\prime}, p)$ over all s' that can be obtained by removing exactly x characters from s. Dreamoon wants to know $\operatorname{ans}(x)$ for all x from 0 to |s| where |s| denotes the length of string s.


-----Input-----

The first line of the input contains the string s (1 ≤ |s| ≤ 2 000).

The second line of the input contains the string p (1 ≤ |p| ≤ 500).

Both strings will only consist of lower case English letters.


-----Output-----

Print |s| + 1 space-separated integers in a single line representing the $\operatorname{ans}(x)$ for all x from 0 to |s|.


-----Examples-----
Input
aaaaa
aa

Output
2 2 1 1 0 0

Input
axbaxxb
ab

Output
0 1 1 2 1 1 0 0



-----Note-----

For the first sample, the corresponding optimal values of s' after removal 0 through |s| = 5 characters from s are {"aaaaa", "aaaa", "aaa", "aa", "a", ""}. 

For the second sample, possible corresponding optimal values of s' are {"axbaxxb", "abaxxb", "axbab", "abab", "aba", "ab", "a", ""}.
"""

def calculate_max_occurrences(s: str, p: str) -> list[int]:
    n = len(s) + 1
    m = len(p)
    d = [[0] * n for _ in range(n)]
    
    for x in range(1, n):
        i, j = x, m
        while i and j:
            j -= s[i - 1] == p[j - 1]
            i -= 1
        if not j:
            for y in range(i + 1):
                d[x][y + x - i - m] = d[i][y] + 1
        for y in range(x):
            d[x][y] = max(d[x][y], d[x - 1][y])
    
    return d[-1]