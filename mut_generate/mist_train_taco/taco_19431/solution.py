"""
QUESTION:
One day Polycarpus got hold of two non-empty strings s and t, consisting of lowercase Latin letters. Polycarpus is quite good with strings, so he immediately wondered, how many different pairs of "x y" are there, such that x is a substring of string s, y is a subsequence of string t, and the content of x and y is the same. Two pairs are considered different, if they contain different substrings of string s or different subsequences of string t. Read the whole statement to understand the definition of different substrings and subsequences.

The length of string s is the number of characters in it. If we denote the length of the string s as |s|, we can write the string as s = s1s2... s|s|.

A substring of s is a non-empty string x = s[a... b] = sasa + 1... sb (1 ≤ a ≤ b ≤ |s|). For example, "code" and "force" are substrings or "codeforces", while "coders" is not. Two substrings s[a... b] and s[c... d] are considered to be different if a ≠ c or b ≠ d. For example, if s="codeforces", s[2...2] and s[6...6] are different, though their content is the same.

A subsequence of s is a non-empty string y = s[p1p2... p|y|] = sp1sp2... sp|y| (1 ≤ p1 < p2 < ... < p|y| ≤ |s|). For example, "coders" is a subsequence of "codeforces". Two subsequences u = s[p1p2... p|u|] and v = s[q1q2... q|v|] are considered different if the sequences p and q are different.

Input

The input consists of two lines. The first of them contains s (1 ≤ |s| ≤ 5000), and the second one contains t (1 ≤ |t| ≤ 5000). Both strings consist of lowercase Latin letters.

Output

Print a single number — the number of different pairs "x y" such that x is a substring of string s, y is a subsequence of string t, and the content of x and y is the same. As the answer can be rather large, print it modulo 1000000007 (109 + 7).

Examples

Input

aa
aa


Output

5


Input

codeforces
forceofcode


Output

60

Note

Let's write down all pairs "x y" that form the answer in the first sample: "s[1...1] t[1]", "s[2...2] t[1]", "s[1...1] t[2]","s[2...2] t[2]", "s[1...2] t[1 2]".
"""

def count_matching_pairs(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    mod = 1000000007
    
    # Convert strings to lists of integers representing their characters
    s = [ord(char) - 97 for char in s]
    t = [ord(char) - 97 for char in t]
    
    # Initialize the dp array
    dp = [[0 for _ in range(n)] for _ in range(26)]
    
    for i in range(m):
        arr = [0 for _ in range(n)]
        for j in range(n):
            if t[i] == s[j]:
                arr[j] = 1
                if j > 0:
                    arr[j] = (arr[j] + dp[s[j - 1]][j - 1]) % mod
        for j in range(n):
            dp[t[i]][j] = (arr[j] + dp[t[i]][j]) % mod
    
    result = 0
    for row in dp:
        for value in row:
            result = (result + value) % mod
    
    return result