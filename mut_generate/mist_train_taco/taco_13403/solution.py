"""
QUESTION:
Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.
NOTE: Prefix and suffix can be overlapping but they should not be equal to the entire string.
Example 1:
Input: s = "abab"
Output: 2
Explanation: "ab" is the longest proper 
prefix and suffix. 
Example 2:
Input: s = "aaaa"
Output: 3
Explanation: "aaa" is the longest proper 
prefix and suffix. 
Your task:
You do not need to read any input or print anything. The task is to complete the function lps(), which takes a string as input and returns an integer. 
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)
Constraints:
1 ≤ |s| ≤ 10^{5}
s contains lower case English alphabets
"""

def longest_proper_prefix_suffix(s: str) -> int:
    lps = [0] * len(s)
    prevLPS, i = 0, 1
    
    while i < len(s):
        if s[prevLPS] == s[i]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    
    return lps[-1]