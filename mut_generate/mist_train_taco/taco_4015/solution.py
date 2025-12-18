"""
QUESTION:
You are given two strings x and y, both consist only of lowercase Latin letters. Let |s| be the length of string s.

Let's call a sequence a a merging sequence if it consists of exactly |x| zeros and exactly |y| ones in some order.

A merge z is produced from a sequence a by the following rules: 

  * if a_i=0, then remove a letter from the beginning of x and append it to the end of z; 
  * if a_i=1, then remove a letter from the beginning of y and append it to the end of z. 



Two merging sequences a and b are different if there is some position i such that a_i ≠ b_i.

Let's call a string z chaotic if for all i from 2 to |z| z_{i-1} ≠ z_i.

Let s[l,r] for some 1 ≤ l ≤ r ≤ |s| be a substring of consecutive letters of s, starting from position l and ending at position r inclusive.

Let f(l_1, r_1, l_2, r_2) be the number of different merging sequences of x[l_1,r_1] and y[l_2,r_2] that produce chaotic merges. Note that only non-empty substrings of x and y are considered.

Calculate ∑ _{1 ≤ l_1 ≤ r_1 ≤ |x| \\\ 1 ≤ l_2 ≤ r_2 ≤ |y|} f(l_1, r_1, l_2, r_2). Output the answer modulo 998 244 353.

Input

The first line contains a string x (1 ≤ |x| ≤ 1000).

The second line contains a string y (1 ≤ |y| ≤ 1000).

Both strings consist only of lowercase Latin letters.

Output

Print a single integer — the sum of f(l_1, r_1, l_2, r_2) over 1 ≤ l_1 ≤ r_1 ≤ |x| and 1 ≤ l_2 ≤ r_2 ≤ |y| modulo 998 244 353.

Examples

Input


aaa
bb


Output


24


Input


code
forces


Output


1574


Input


aaaaa
aaa


Output


0


Input


justamassivetesttocheck
howwellyouhandlemodulooperations


Output


667387032

Note

In the first example there are: 

  * 6 pairs of substrings "a" and "b", each with valid merging sequences "01" and "10"; 
  * 3 pairs of substrings "a" and "bb", each with a valid merging sequence "101"; 
  * 4 pairs of substrings "aa" and "b", each with a valid merging sequence "010"; 
  * 2 pairs of substrings "aa" and "bb", each with valid merging sequences "0101" and "1010"; 
  * 2 pairs of substrings "aaa" and "b", each with no valid merging sequences; 
  * 1 pair of substrings "aaa" and "bb" with a valid merging sequence "01010"; 



Thus, the answer is 6 ⋅ 2 + 3 ⋅ 1 + 4 ⋅ 1 + 2 ⋅ 2 + 2 ⋅ 0 + 1 ⋅ 1 = 24.
"""

def calculate_chaotic_merges(x: str, y: str) -> int:
    x = list(map(lambda ch: ord(ch) - 97, x))
    y = list(map(lambda ch: ord(ch) - 97, y))
    ans = 0
    mod = 998244353
    m, n = len(x), len(y)
    
    v1 = [1] * (m + 1)
    v2 = [1] * (n + 1)
    
    for i in range(m - 2, -1, -1):
        if x[i] != x[i + 1]:
            v1[i] += v1[i + 1]
    
    for i in range(n - 2, -1, -1):
        if y[i] != y[i + 1]:
            v2[i] += v2[i + 1]
    
    dp = [[[0] * 27 for j in range(n + 1)] for i in range(m + 1)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            for k in range(27):
                if x[i] == k:
                    if y[j] != k:
                        dp[i][j][k] = (dp[i][j + 1][y[j]] + v1[i]) % mod
                elif y[j] == k:
                    dp[i][j][k] = (dp[i + 1][j][x[i]] + v2[j]) % mod
                else:
                    dp[i][j][k] = (dp[i + 1][j][x[i]] + dp[i][j + 1][y[j]] + (x[i] != y[j]) * (v2[j] + v1[i])) % mod
    
    for i in range(m):
        for j in range(n):
            ans = (ans + dp[i][j][26]) % mod
    
    return ans