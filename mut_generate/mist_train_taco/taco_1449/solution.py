"""
QUESTION:
You are given a string $s$ of length $n$ consisting of lowercase Latin letters. You may apply some operations to this string: in one operation you can delete some contiguous substring of this string, if all letters in the substring you delete are equal. For example, after deleting substring bbbb from string abbbbaccdd we get the string aaccdd.

Calculate the minimum number of operations to delete the whole string $s$.


-----Input-----

The first line contains one integer $n$ ($1 \le n \le 500$) — the length of string $s$.

The second line contains the string $s$ ($|s| = n$) consisting of lowercase Latin letters.


-----Output-----

Output a single integer — the minimal number of operation to delete string $s$.


-----Examples-----
Input
5
abaca

Output
3
Input
8
abcddcba

Output
4
"""

def min_operations_to_delete_string(s: str, n: int = None) -> int:
    if n is None:
        n = len(s)
    
    # Preprocess the string to remove consecutive duplicates
    ss = ''
    re = ''
    for i in range(n):
        if re != s[i]:
            ss += re
            re = s[i]
    ss += re
    
    a = ss
    N = len(a)
    
    # Initialize the dp array
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Fill the dp array
    for l in range(1, N + 1):
        i = 0
        j = l - 1
        while j < N:
            if l == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 1 + dp[i + 1][j]
                for K in range(i + 1, j + 1):
                    if a[i] == a[K]:
                        if dp[i][j] >= dp[i][K - 1] + dp[K + 1][j]:
                            dp[i][j] = dp[i][K - 1] + dp[K + 1][j]
            i += 1
            j += 1
    
    return dp[0][N - 1]