"""
QUESTION:
You are given two strings s and t. Now your task is to print all longest common sub-sequences in lexicographical order.
Example 1:
Input: s = abaaa, t = baabaca
Output: aaaa abaa baaa
Example 2:
Input: s = aaa, t = a
Output: a
Your Task:
You do not need to read or print anything. Your task is to complete the function all_longest_common_subsequences() which takes string a and b as first and second parameter respectively and returns a list of strings which contains all possible longest common subsequences in lexicographical order.
 
Expected Time Complexity: O(n^{4})
Expected Space Complexity: O(K * n) where K is a constant less than n.
 
Constraints:
1 ≤ Length of both strings ≤ 50
"""

def all_longest_common_subsequences(s, t):
    n = len(s)
    m = len(t)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    maxi = dp[n][m]
    
    def printing(i, j, temp, res, maxi):
        if maxi == 0:
            if temp not in res:
                res.append(temp)
            return
        if i >= len(s) or j >= len(t):
            return
        for row in range(i, len(s)):
            for col in range(j, len(t)):
                if s[row] == t[col]:
                    temp += s[row]
                    printing(row + 1, col + 1, temp, res, maxi - 1)
                    temp = temp[:-1]
    
    res = []
    printing(0, 0, '', res, maxi)
    res.sort()
    return res