"""
QUESTION:
You are given a string $s$ consisting of exactly $n$ characters, and each character is either '0', '1' or '2'. Such strings are called ternary strings.

Your task is to replace minimum number of characters in this string with other characters to obtain a balanced ternary string (balanced ternary string is a ternary string such that the number of characters '0' in this string is equal to the number of characters '1', and the number of characters '1' (and '0' obviously) is equal to the number of characters '2').

Among all possible balanced ternary strings you have to obtain the lexicographically (alphabetically) smallest.

Note that you can neither remove characters from the string nor add characters to the string. Also note that you can replace the given characters only with characters '0', '1' and '2'.

It is guaranteed that the answer exists.


-----Input-----

The first line of the input contains one integer $n$ ($3 \le n \le 3 \cdot 10^5$, $n$ is divisible by $3$) — the number of characters in $s$.

The second line contains the string $s$ consisting of exactly $n$ characters '0', '1' and '2'.


-----Output-----

Print one string — the lexicographically (alphabetically) smallest balanced ternary string which can be obtained from the given one with minimum number of replacements.

Because $n$ is divisible by $3$ it is obvious that the answer exists. And it is obvious that there is only one possible answer.


-----Examples-----
Input
3
121

Output
021

Input
6
000000

Output
001122

Input
6
211200

Output
211200

Input
6
120110

Output
120120
"""

def balance_ternary_string(n: int, s: str) -> str:
    s = list(s)
    cnt_0 = s.count('0')
    cnt_1 = s.count('1')
    cnt_2 = s.count('2')
    k = n // 3
    d = {'0': cnt_0, '1': cnt_1, '2': cnt_2}
    
    # First pass: Replace from the beginning to balance '0' and '1'
    for i in range(n):
        if d[s[i]] > k:
            if s[i] == '1' and cnt_1 > k:
                if cnt_0 < k:
                    s[i] = '0'
                    cnt_0 += 1
                    cnt_1 -= 1
            elif s[i] == '2' and cnt_2 > k:
                if cnt_0 < k:
                    s[i] = '0'
                    cnt_0 += 1
                    cnt_2 -= 1
                elif cnt_1 < k:
                    s[i] = '1'
                    cnt_1 += 1
                    cnt_2 -= 1
    
    # Second pass: Replace from the end to balance '2'
    for j in range(n - 1, -1, -1):
        if d[s[j]] > k:
            if s[j] == '0' and cnt_0 > k:
                if cnt_2 < k:
                    s[j] = '2'
                    cnt_2 += 1
                    cnt_0 -= 1
                elif cnt_1 < k:
                    s[j] = '1'
                    cnt_1 += 1
                    cnt_0 -= 1
            elif s[j] == '1' and cnt_1 > k:
                if cnt_2 < k:
                    s[j] = '2'
                    cnt_2 += 1
                    cnt_1 -= 1
    
    return ''.join(s)