"""
QUESTION:
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.



Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.




Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

def longest_repeating_substring_after_replacements(s: str, k: int) -> int:
    if not s:
        return 0
    
    count = {}
    lo = 0
    max_letter = 0
    max_length = 0
    
    for hi in range(len(s)):
        count[s[hi]] = count.get(s[hi], 0) + 1
        max_letter = max(max_letter, count[s[hi]])
        
        if (hi - lo + 1) - max_letter > k:
            count[s[lo]] -= 1
            lo += 1
        
        max_length = max(max_length, hi - lo + 1)
    
    return max_length