"""
QUESTION:
Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.
Example 1:
Input: str = "ababbbabbababa"
Output: 3
Explaination: After 3 partitioning substrings 
are "a", "babbbab", "b", "ababa".
Example 2:
Input: str = "aaabba"
Output: 1
Explaination: The substrings after 1
partitioning are "aa" and "abba".
Your Task:
You do not need to read input or print anything, Your task is to complete the function palindromicPartition() which takes the string str as the input parameter and returns the minimum number of partitions required.
Expected Time Complexity: O(n*n) [n is the length of the string str]
Expected Auxiliary Space: O(n*n)
Constraints:
1 ≤ length of str ≤ 500
"""

def min_palindrome_partitions(s: str) -> int:
    def is_palindrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def dfs(s, i, j, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        if i >= j:
            return 0
        if is_palindrome(s, i, j):
            return 0
        mx = len(s)
        for k in range(i, j):
            if is_palindrome(s, i, k):
                t = dfs(s, k + 1, j, dp) + 1
                mx = min(mx, t)
        dp[i][j] = mx
        return dp[i][j]

    n = len(s)
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    return dfs(s, 0, n - 1, dp)