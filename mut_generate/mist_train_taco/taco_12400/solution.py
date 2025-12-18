"""
QUESTION:
We have a string s of length n, which contains only UPPERCASE characters and we have a number k (always less than n). We can make at most k changes in our string. In one change, you can replace any s[i] (0<= i < n) with any uppercase character (from 'A' to 'Z'). After k changes, find the maximum possible length of the sub-string which have all same characters.
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Change 2 'B' into 'A'. 
Now s = "AAAA"
Example:
Input: s = "ADBD", k = 1
Output: 3
Explanation: Change 'B' into 'D'.
Now s = "ADDD"
Your Task:
You don't need to read or print anything. Your task is to complete the function characterReplacement() which takes s and k as input parameters and returns the maximum length of sub-string after doing k changes.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(26)
 
Constraints:
1 <= n <= 10^{5}
0 <= k < n
"""

def characterReplacement(s: str, k: int) -> int:
    lookup = {}
    maxCount = 0
    i = 0
    j = 0
    res = 0
    
    for j in range(len(s)):
        lookup[s[j]] = 1 + lookup.get(s[j], 0)
        maxCount = max(maxCount, lookup[s[j]])
        
        while j - i + 1 - maxCount > k:
            lookup[s[i]] -= 1
            i += 1
        
        res = max(res, j - i + 1)
    
    return res