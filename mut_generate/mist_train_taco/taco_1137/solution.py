"""
QUESTION:
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.
 
Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
Input: s = "triplepillooooow"
Output: 5

Example 4:
Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:
Input: s = "tourist"
Output: 1

 
Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
"""

def max_power_of_string(s: str) -> int:
    n = len(s)
    count = 0
    cur_count = 1
    
    for i in range(n):
        if i < n - 1 and s[i] == s[i + 1]:
            cur_count += 1
        else:
            if cur_count > count:
                count = cur_count
            cur_count = 1
    
    return count