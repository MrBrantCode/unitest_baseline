"""
QUESTION:
You are given two strings $s$ and $t$, each of length $n$ and consisting of lowercase Latin alphabets. You want to make $s$ equal to $t$. 

You can perform the following operation on $s$ any number of times to achieve it —   Choose any substring of $s$ and rotate it clockwise once, that is, if the selected substring is $s[l,l+1...r]$, then it becomes $s[r,l,l + 1 ... r - 1]$. All the remaining characters of $s$ stay in their position. 

For example, on rotating the substring $[2,4]$ , string "abcde" becomes "adbce". 

A string $a$ is a substring of a string $b$ if $a$ can be obtained from $b$ by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

Find the minimum number of operations required to convert $s$ to $t$, or determine that it's impossible.


-----Input-----

The first line of the input contains a single integer $t$ $(1\leq t \leq 2000)$ — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer $n$ $(1\leq n \leq 2000)$ — the length of the strings. 

The second and the third lines contain strings $s$ and $t$ respectively.

The sum of $n$ over all the test cases does not exceed $2000$.


-----Output-----

For each test case, output the minimum number of operations to convert $s$ to $t$. If it is not possible to convert $s$ to $t$, output $-1$ instead.


-----Example-----
Input
6
1
a
a
2
ab
ba
3
abc
cab
3
abc
cba
4
abab
baba
4
abcc
aabc

Output
0
1
1
2
1
-1



-----Note-----

For the $1$-st test case, since $s$ and $t$ are equal, you don't need to apply any operation.

For the $2$-nd test case, you only need to apply one operation on the entire string ab to convert it to ba.

For the $3$-rd test case, you only need to apply one operation on the entire string abc to convert it to cab.

For the $4$-th test case, you need to apply the operation twice: first on the entire string abc to convert it to cab and then on the substring of length $2$ beginning at the second character to convert it to cba.

For the $5$-th test case, you only need to apply one operation on the entire string abab to convert it to baba.

For the $6$-th test case, it is not possible to convert string $s$ to $t$.
"""

def min_operations_to_convert_strings(s: str, t: str) -> int:
    n = len(s)
    
    # Check if it's possible to convert s to t by comparing sorted versions
    if sorted(s) != sorted(t):
        return -1
    
    # Initialize count arrays for characters in s and t
    s_count = [[0 for _ in range(n + 1)] for _ in range(26)]
    t_count = [[0 for _ in range(n + 1)] for _ in range(26)]
    
    for i in range(n):
        for j in range(26):
            s_count[j][i] = s_count[j][i - 1]
            t_count[j][i] = t_count[j][i - 1]
        s_count[ord(s[i]) - ord('a')][i] += 1
        t_count[ord(t[i]) - ord('a')][i] += 1
    
    # Initialize dp array
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(i, n):
            dp[i][j] = dp[i - 1][j] + 1
            if s[i] == t[j]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            c = ord(t[j]) - ord('a')
            if s_count[c][i] < t_count[c][j]:
                dp[i][j] = min(dp[i][j], dp[i][j - 1])
    
    return dp[n - 1][n - 1]