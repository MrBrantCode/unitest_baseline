"""
QUESTION:
G: Palindromic Subsequences

problem

Given a string S consisting only of lowercase letters, find out how many subsequences of this string S are not necessarily continuous and are palindromes.

Here, a subsequence that is not necessarily continuous with S is an arbitrary selection of one or more characters | S | characters or less from the original character string S (the position of each character to be selected may be discontinuous), and they are used. Refers to a character string created by concatenating the characters in the original order. Note that an empty string is not allowed as a subsequence in this issue.

Also, if the string X is a palindrome, it means that the original string X and the inverted X string X'are equal.

Also note that even if the same palindrome is generated as a result of different subsequence arrangements, it will not be counted twice. For example, if S = `acpc`, both the subsequence consisting of only the second character and the subsequence consisting of only the fourth character are palindromes` c`, but this cannot be repeated multiple times, only once in total. I will count it.

The answer can be very large, so print the remainder divided by 1,000,000,007.

Input format


S

Constraint

* 1 \ leq | S | \ leq 2,000
* S contains only lowercase letters



Output format

* Output the remainder of the answer divided by 1,000,000,007 on one line.



Input example 1


acpc

Output example 1


Five

There are five types of subsequences of the string `acpc` that are not necessarily continuous and are palindromes:` a`, `c`,` cc`, `cpc`, and` p`. Note that we count the number of substring types.

Input example 2


z

Output example 2


1

The only subsequence that meets the condition is `z`. Note that an empty string is not allowed as a subsequence.

Input example 3


madokamagica

Output example 3


28





Example

Input

acpc


Output

5
"""

def count_palindromic_subsequences(s: str) -> int:
    from bisect import bisect_left as bl
    from bisect import bisect_right as br
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = len(s)
    alpha2 = {j: i for (i, j) in enumerate(alpha)}
    memo = [[] for _ in range(26)]
    mod = 10**9 + 7
    
    for i in range(l):
        memo[alpha2[s[i]]].append(i)
    
    dp = [[0] * (l + 1) for _ in range(l + 1)]
    dp[0][l] = 1
    ans = 0
    
    for i in range(l):
        for j in range(i + 1, l + 1):
            p = dp[i][j]
            if p == 0:
                continue
            for k in range(26):
                x = bl(memo[k], i)
                y = br(memo[k], j - 1) - 1
                if x > y:
                    continue
                ans += p
                if x < y:
                    (mx, my) = (memo[k][x], memo[k][y])
                    dp[mx + 1][my] = (dp[mx + 1][my] + p) % mod
            ans = ans % mod
    
    ans = (ans + sum([sum([i for i in j]) % mod for j in dp]) + mod - 1) % mod
    return ans