"""
QUESTION:
You are given a string $s$ of length $n$ consisting only of lowercase Latin letters.

A substring of a string is a contiguous subsequence of that string. So, string "forces" is substring of string "codeforces", but string "coder" is not.

Your task is to calculate the number of ways to remove exactly one substring from this string in such a way that all remaining characters are equal (the number of distinct characters either zero or one).

It is guaranteed that there is at least two different characters in $s$.

Note that you can remove the whole string and it is correct. Also note that you should remove at least one character.

Since the answer can be rather large (not very large though) print it modulo $998244353$.

If you are Python programmer, consider using PyPy instead of Python when you submit your code.


-----Input-----

The first line of the input contains one integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the length of the string $s$.

The second line of the input contains the string $s$ of length $n$ consisting only of lowercase Latin letters.

It is guaranteed that there is at least two different characters in $s$.


-----Output-----

Print one integer — the number of ways modulo $998244353$ to remove exactly one substring from $s$ in such way that all remaining characters are equal.


-----Examples-----
Input
4
abaa

Output
6

Input
7
aacdeee

Output
6
Input
2
az

Output
3


-----Note-----

Let $s[l; r]$ be the substring of $s$ from the position $l$ to the position $r$ inclusive.

Then in the first example you can remove the following substrings:   $s[1; 2]$;  $s[1; 3]$;  $s[1; 4]$;  $s[2; 2]$;  $s[2; 3]$;  $s[2; 4]$. 

In the second example you can remove the following substrings:   $s[1; 4]$;  $s[1; 5]$;  $s[1; 6]$;  $s[1; 7]$;  $s[2; 7]$;  $s[3; 7]$. 

In the third example you can remove the following substrings:   $s[1; 1]$;  $s[1; 2]$;  $s[2; 2]$.
"""

def count_ways_to_remove_substring(n: int, s: str) -> int:
    MOD = 998244353
    
    # Count the number of leading characters that are the same
    st = 0
    for i in range(n):
        if s[i] == s[0]:
            st += 1
        else:
            break
    
    # Count the number of trailing characters that are the same
    en = 0
    for i in range(n-1, -1, -1):
        if s[i] == s[-1]:
            en += 1
        else:
            break
    
    # Calculate the number of ways based on the first and last characters
    if s[0] != s[-1]:
        return (en + st + 1) % MOD
    else:
        return ((en + 1) * (st + 1)) % MOD