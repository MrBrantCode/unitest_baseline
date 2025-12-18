"""
QUESTION:
Given two strings S1 and S2, Count no. of all subsequences of string S1 that are equal to string S2.
Example 1:
Input: 
S1 = geeksforgeeks
S2 = gks
Output: 4
Explaination: We can pick characters from S1 as a subsequence from indices {0,3,4}, {0,3,12}, {0,11,12} and {8,11,12}.So total 4 subsequences of S1 that are equal to S2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countWays() which takes the string S1 and S2 as input parameters and returns the number of desired subsequences.
Expected Time Complexity: O(n*m)        [n and m are length of the strings]
Expected Auxiliary Space: O(n*m)
Constraints:
1 ≤ n, m ≤ 500
"""

def count_subsequences(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    def answer(i: int, j: int) -> int:
        if j == -1:
            return 1
        if i == -1:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = answer(i - 1, j - 1) + answer(i - 1, j)
        else:
            dp[i][j] = answer(i - 1, j)
        return dp[i][j]
    
    return answer(n - 1, m - 1)