"""
QUESTION:
A subsequence of a string S is a string that can be obtained by deleting zero or more characters from S without changing the order of the remaining characters.
For example, arc, artistic and (an empty string) are all subsequences of artistic; abc and ci are not.
You are given a string A consisting of lowercase English letters.
Find the shortest string among the strings consisting of lowercase English letters that are not subsequences of A.
If there are more than one such string, find the lexicographically smallest one among them.

-----Constraints-----
 - 1 \leq |A| \leq 2 \times 10^5
 - A consists of lowercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
A

-----Output-----
Print the lexicographically smallest string among the shortest strings consisting of lowercase English letters that are not subsequences of A.

-----Sample Input-----
atcoderregularcontest

-----Sample Output-----
b

The string atcoderregularcontest contains a as a subsequence, but not b.
"""

def find_shortest_non_subsequence(A: str) -> str:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = len(A)
    alpha2 = {j: i for (i, j) in enumerate(alpha)}
    memo = [[0] * 26 for _ in range(l, -1, -1)]
    
    for i in range(26):
        memo[l][i] = l + 1
    
    for (x, y) in alpha2.items():
        for i in range(l - 1, -1, -1):
            if A[i] == x:
                memo[i][y] = i + 1
            else:
                memo[i][y] = memo[i + 1][y]
    
    search = [1] * (l + 2)
    search[l + 1] = 0
    
    for i in range(l - 1, -1, -1):
        m = max([memo[i][j] for j in range(26)])
        if m != l + 1:
            search[i] = search[m] + 1
    
    (n, seq) = (0, 0)
    ans_len = search[0]
    ans = ''
    temp = 0
    
    for i in range(ans_len):
        for j in range(26):
            n = memo[temp][j]
            seq = search[n] + i
            if seq + 1 == ans_len:
                ans += alpha[j]
                temp = memo[temp][j]
                break
    
    return ans