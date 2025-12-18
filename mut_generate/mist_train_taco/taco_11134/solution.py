"""
QUESTION:
Given two strings X and Y, and two values costX and costY, the task is to find the minimum cost required to make the given two strings identical. You can delete characters from both the strings. The cost of deleting a character from string X is costX and from Y is costY. The cost of removing all characters from a string is the same.
Example 1:
Input: X = "abcd", Y = "acdb", costX = 10 
       costY = 20.
Output: 30
Explanation: For Making both strings 
identical we have to delete character 
'b' from both the string, hence cost 
will be = 10 + 20 = 30.
Example 2:
Input : X = "ef", Y = "gh", costX = 10
        costY = 20.
Output: 60
Explanation: For making both strings 
identical, we have to delete 2-2 
characters from both the strings, hence 
cost will be = 10 + 10 + 20 + 20 = 60.
Your Task:
You don't need to read or print anything. Your task is to complete the function findMinCost() which takes both strings and the costs as input parameters and returns the minimum cost.
Expected Time Complexity: O(|X|*|Y|)
Expected Space Complexity: O(|X|*|Y|)
Constraints:
1 ≤ |X|, |Y| ≤ 1000
"""

def find_min_cost(X: str, Y: str, costX: int, costY: int) -> int:
    def longest_common_substring(a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        def lcs(a: str, b: str, i: int, j: int) -> int:
            if i == len(a) or j == len(b):
                dp[i][j] = 0
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if a[i] == b[j]:
                dp[i][j] = 1 + lcs(a, b, i + 1, j + 1)
            else:
                dp[i][j] = max(lcs(a, b, i, j + 1), lcs(a, b, i + 1, j))
            return dp[i][j]
        
        return lcs(a, b, 0, 0)

    lcs_length = longest_common_substring(X, Y)
    n, m = len(X), len(Y)
    min_cost = (n - lcs_length) * costX + (m - lcs_length) * costY
    return min_cost