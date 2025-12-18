"""
QUESTION:
Returning back to problem solving, Gildong is now studying about palindromes. He learned that a palindrome is a string that is the same as its reverse. For example, strings "pop", "noon", "x", and "kkkkkk" are palindromes, while strings "moon", "tv", and "abab" are not. An empty string is also a palindrome.

Gildong loves this concept so much, so he wants to play with it. He has $n$ distinct strings of equal length $m$. He wants to discard some of the strings (possibly none or all) and reorder the remaining strings so that the concatenation becomes a palindrome. He also wants the palindrome to be as long as possible. Please help him find one.


-----Input-----

The first line contains two integers $n$ and $m$ ($1 \le n \le 100$, $1 \le m \le 50$) — the number of strings and the length of each string.

Next $n$ lines contain a string of length $m$ each, consisting of lowercase Latin letters only. All strings are distinct.


-----Output-----

In the first line, print the length of the longest palindrome string you made.

In the second line, print that palindrome. If there are multiple answers, print any one of them. If the palindrome is empty, print an empty line or don't print this line at all.


-----Examples-----
Input
3 3
tab
one
bat

Output
6
tabbat

Input
4 2
oo
ox
xo
xx

Output
6
oxxxxo

Input
3 5
hello
codef
orces

Output
0


Input
9 4
abab
baba
abcd
bcde
cdef
defg
wxyz
zyxw
ijji

Output
20
ababwxyzijjizyxwbaba



-----Note-----

In the first example, "battab" is also a valid answer.

In the second example, there can be 4 different valid answers including the sample output. We are not going to provide any hints for what the others are.

In the third example, the empty string is the only valid palindrome string.
"""

def find_longest_palindrome(n, m, strings):
    s = dict()
    z = []
    
    for a in strings:
        b = a[::-1]
        if a not in s and b not in s:
            s[a] = 1
        elif a in s:
            s[a] += 1
        elif b in s:
            s[b] += 1
        if b == a:
            z.append(a)
    
    count = 0
    data = list(s.keys())
    ans = ''
    
    for i in data:
        c = s[i] // 2
        ans += i * c
        count += c * 2
        s[i] %= 2
    
    if count == 0 and len(z) == 0:
        return 0, ''
    
    ans1 = ans[::-1]
    for i in range(len(z)):
        if s[z[i]] >= 1:
            ans += z[i]
            count += 1
            break
    
    return m * count, ans + ans1