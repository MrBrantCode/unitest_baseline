"""
QUESTION:
Given a string S, find the longest repeating non-overlapping substring in it. In other words find 2 identical substrings of maximum length which do not overlap. If there exists more than one such substring return any of them.  Print the longest non-overlapping substring. If no such substring exists print -1.
Note: Multiple Answers are possible but you have to print the substring which occurs atleat twice first.
For Example: "ablhiabohi". Here both "ab" and "hi" are possible answers. But you will have to return "ab" as because it repeats before "hi".
 
Example 1:
Input:
N = 13
S = "geeksforgeeks"
Output:
geeks
Explanation:
The string "geeks" is the longest Substring
of S which is repeating but not overlapping.
Example 2:
Input:
N = 8
S = "heyhheyi"
Output:
hey
Explanation:
The string "hey" is the longest Substring
of S which is repeating but not overlapping.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestSubstring() which takes a Integer N and a String S as input and returns the answer.
 
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
1 <= N <= 10^{3}
"""

def longest_repeating_non_overlapping_substring(S, N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    max_len = 0
    res = ''
    
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == S[j] and dp[i][j] < j - i:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
                if dp[i + 1][j + 1] > max_len:
                    max_len = dp[i + 1][j + 1]
                    res = S[i - max_len + 1:i + 1]
    
    return res if len(res) > 0 else -1