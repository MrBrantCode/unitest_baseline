"""
QUESTION:
Given two strings, $a$ and $\boldsymbol{b}$, find and print the total number of ways to insert a character at any position in string $\class{ML__boldsymbol}{\boldsymbol{a}}$ such that the length of the Longest Common Subsequence of characters in the two strings increases by one.

Input Format

The first line contains a single string denoting $\class{ML__boldsymbol}{\boldsymbol{a}}$. 

The second line contains a single string denoting $\boldsymbol{b}$.

Constraints

Scoring     

$1\leq|a|,|b|\leq5000$
Strings $\class{ML__boldsymbol}{\boldsymbol{a}}$ and $\boldsymbol{b}$ are alphanumeric (i.e., consisting of arabic digits and/or upper and lower case English letters).
The new character being inserted must also be alphanumeric (i.e., a digit or upper/lower case English letter).

Subtask     

$1\le|a|,|b|\le1000$ for $\boldsymbol{66.67\%}$ of the maximum score.  

Output Format

Print a single integer denoting the total number of ways to insert a character into string $\class{ML__boldsymbol}{\boldsymbol{a}}$ in such a way that the length of the longest common subsequence of $\class{ML__boldsymbol}{\boldsymbol{a}}$ and $\boldsymbol{b}$ increases by one.

Sample Input
aa
baaa

Sample Output
4

Explanation

The longest common subsequence shared by $a=\text{"a}\textbf{a}$ and $b=\text{"baaa''}$ is aa, which has a length of $2$. There are two ways that the length of the longest common subsequence can be increased to $3$ by adding a single character to $\class{ML__boldsymbol}{\boldsymbol{a}}$:

There are $3$ different positions in string $\class{ML__boldsymbol}{\boldsymbol{a}}$ where we could insert an additional a to create longest common subsequence aaa (i.e., at the beginning, middle, and end of the string). 
We can insert a b at the beginning of the string for a new longest common subsequence of baa.

As we have $3+1=4$ ways to insert an alphanumeric character into $\class{ML__boldsymbol}{\boldsymbol{a}}$ and increase the length of the longest common subsequence by one, we print $\begin{array}{c}4\end{array}$ on a new line.
"""

import string

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp

def alpIndexes(s, alp):
    d = dict()
    for letter in alp:
        d[letter] = []
    for i in range(len(s)):
        d[s[i]].append(i)
    return d

def count_ways_to_increase_lcs(a, b):
    n = len(a)
    m = len(b)
    chars = list(string.ascii_lowercase)
    charIndexes = alpIndexes(b, chars)
    dpl = lcs(a, b)
    dpr = lcs(a[::-1], b[::-1])
    lcs_length = dpl[n][m]
    ans = 0
    for i in range(0, n + 1):
        for letter in chars:
            for j in charIndexes[letter]:
                if dpl[i][j] + dpr[n - i][m - j - 1] == lcs_length:
                    ans += 1
                    break
    return ans