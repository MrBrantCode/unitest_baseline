"""
QUESTION:
Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.
Example 1:
Input:
S = "aabacbebebe", K = 3
Output: 7
Explanation: "cbebebe" is the longest 
substring with K distinct characters.
Example 2:
Input: 
S = "aaaa", K = 2
Output: -1
Explanation: There's no substring with K
distinct characters.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestKSubstr() which takes the string S and an integer K as input and returns the length of the longest substring with exactly K distinct characters. If there is no substring with exactly K distinct characters then return -1.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).
Constraints:
1 ≤ |S| ≤ 10^{5}
1 ≤ K ≤ 10^{5}
All characters are lowercase latin characters.
"""

def longest_k_substr(s: str, k: int) -> int:
    l = 0
    count = {}
    maxLen = float('-inf')
    
    for r in range(len(s)):
        if s[r] not in count:
            count[s[r]] = 0
        count[s[r]] += 1
        
        while len(count) > k:
            count[s[l]] -= 1
            if count[s[l]] == 0:
                del count[s[l]]
            l += 1
        
        if len(count) == k:
            maxLen = max(maxLen, r - l + 1)
    
    return -1 if maxLen == float('-inf') else maxLen