"""
QUESTION:
The only difference between easy and hard versions is the length of the string.

You are given a string $s$ and a string $t$, both consisting only of lowercase Latin letters. It is guaranteed that $t$ can be obtained from $s$ by removing some (possibly, zero) number of characters (not necessary contiguous) from $s$ without changing order of remaining characters (in other words, it is guaranteed that $t$ is a subsequence of $s$).

For example, the strings "test", "tst", "tt", "et" and "" are subsequences of the string "test". But the strings "tset", "se", "contest" are not subsequences of the string "test".

You want to remove some substring (contiguous subsequence) from $s$ of maximum possible length such that after removing this substring $t$ will remain a subsequence of $s$.

If you want to remove the substring $s[l;r]$ then the string $s$ will be transformed to $s_1 s_2 \dots s_{l-1} s_{r+1} s_{r+2} \dots s_{|s|-1} s_{|s|}$ (where $|s|$ is the length of $s$).

Your task is to find the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.


-----Input-----

The first line of the input contains one string $s$ consisting of at least $1$ and at most $2 \cdot 10^5$ lowercase Latin letters.

The second line of the input contains one string $t$ consisting of at least $1$ and at most $2 \cdot 10^5$ lowercase Latin letters.

It is guaranteed that $t$ is a subsequence of $s$.


-----Output-----

Print one integer — the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.


-----Examples-----
Input
bbaba
bb

Output
3

Input
baaba
ab

Output
2

Input
abcde
abcde

Output
0

Input
asdfasdf
fasd

Output
3
"""

def max_removable_substring_length(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    
    # Array to store the rightmost positions of characters in t in s
    rg = [0] * m
    j = m - 1
    for i in range(n):
        if s[n - 1 - i] == t[j]:
            rg[j] = n - 1 - i
            if j == 0:
                break
            j -= 1
    
    # Array to store the leftmost positions of characters in t in s
    lg = [0] * m
    j = 0
    for i in range(n):
        if s[i] == t[j]:
            lg[j] = i
            if j == m - 1:
                break
            j += 1
    
    # Calculate the maximum length of the removable substring
    mx = max(rg[0], n - 1 - lg[-1])
    for j in range(1, m):
        mx = max(mx, rg[j] - lg[j - 1] - 1)
    
    return mx