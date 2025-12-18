"""
QUESTION:
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
 
Example 1:
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:
Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.

Example 3:
Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

 
Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
"""

def find_longest_even_vowel_substring(s: str) -> int:
    s = s + 'a'  # Append a character to handle edge cases
    bits = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    dp = {0: -1}  # Initialize the dp dictionary with the initial state
    res = 0
    key = 0
    
    for i, char in enumerate(s):
        if char in bits:
            if key in dp:
                res = max(res, i - dp[key] - 1)
            key = key ^ (1 << bits[char])
            if key not in dp:
                dp[key] = i
    
    return res