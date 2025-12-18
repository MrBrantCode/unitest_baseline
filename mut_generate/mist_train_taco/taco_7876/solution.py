"""
QUESTION:
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
Return 0 if the string is already balanced.
 
Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 

Example 4:
Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".

 
Constraints:

1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.
"""

from collections import Counter

def find_min_replacement_length(s: str) -> int:
    if len(s) % 4 != 0:
        return -1
    
    target_count = len(s) // 4
    char_count = Counter(s)
    
    if all(char_count[c] == target_count for c in 'QWER'):
        return 0
    
    min_length = len(s)
    left = 0
    
    for right in range(len(s)):
        char_count[s[right]] -= 1
        
        while left <= right and all(char_count[c] <= target_count for c in 'QWER'):
            min_length = min(min_length, right - left + 1)
            char_count[s[left]] += 1
            left += 1
    
    return min_length