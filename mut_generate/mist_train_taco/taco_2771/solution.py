"""
QUESTION:
Given a binary string s (a string consisting only of '0' and '1's).
Return the number of substrings with all characters 1's.
Since the answer may be too large, return it modulo 10^9 + 7.
 
Example 1:
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:
Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.

Example 3:
Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.

Example 4:
Input: s = "000"
Output: 0

 
Constraints:

s[i] == '0' or s[i] == '1'
1 <= s.length <= 10^5
"""

def count_all_ones_substrings(s: str) -> int:
    MOD = 10**9 + 7
    dic = {}
    n = len(s)
    left = 0
    
    while left < n:
        if s[left] == '1':
            right = left
            while right < n and s[right] == '1':
                right += 1
            length = right - left
            if length in dic:
                dic[length] += 1
            else:
                dic[length] = 1
            left = right
        else:
            left += 1
    
    total = 0
    for length, count in dic.items():
        total = (total + length * (length + 1) // 2 * count) % MOD
    
    return total