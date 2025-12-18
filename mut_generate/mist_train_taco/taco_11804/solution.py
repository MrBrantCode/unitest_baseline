"""
QUESTION:
You are given two strings s and t consisting of small Latin letters, string s can also contain '?' characters. 

Suitability of string s is calculated by following metric:

Any two letters can be swapped positions, these operations can be performed arbitrary number of times over any pair of positions. Among all resulting strings s, you choose the one with the largest number of non-intersecting occurrences of string t. Suitability is this number of occurrences.

You should replace all '?' characters with small Latin letters in such a way that the suitability of string s is maximal.


-----Input-----

The first line contains string s (1 ≤ |s| ≤ 10^6).

The second line contains string t (1 ≤ |t| ≤ 10^6).


-----Output-----

Print string s with '?' replaced with small Latin letters in such a way that suitability of that string is maximal.

If there are multiple strings with maximal suitability then print any of them.


-----Examples-----
Input
?aa?
ab

Output
baab

Input
??b?
za

Output
azbz

Input
abcd
abacaba

Output
abcd



-----Note-----

In the first example string "baab" can be transformed to "abab" with swaps, this one has suitability of 2. That means that string "baab" also has suitability of 2.

In the second example maximal suitability you can achieve is 1 and there are several dozens of such strings, "azbz" is just one of them.

In the third example there are no '?' characters and the suitability of the string is 0.
"""

from collections import Counter

def maximize_suitability(s: str, t: str) -> str:
    s_cnt = Counter(s)
    t_cnt = Counter(t)
    hatena = s_cnt['?']
    
    (ok, ng) = (0, 10 ** 6 + 1)
    
    while abs(ok - ng) > 1:
        mid = ok + ng >> 1
        req = 0
        for k, v in t_cnt.items():
            req += max(0, v * mid - s_cnt[k])
        if req <= hatena:
            ok = mid
        else:
            ng = mid
    
    keys = list(t_cnt.keys())
    s = list(s)
    
    for i in range(len(s)):
        if s[i] != '?':
            continue
        while keys and t_cnt[keys[-1]] * ok <= s_cnt[keys[-1]]:
            keys.pop()
        if keys:
            s[i] = keys[-1]
            s_cnt[keys[-1]] += 1
        else:
            s[i] = 'a'
    
    return ''.join(s)