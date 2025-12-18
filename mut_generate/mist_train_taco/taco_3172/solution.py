"""
QUESTION:
Given a non-empty string s, you may delete at most one character.  Judge whether you can make it a palindrome.


Example 1:

Input: "aba"
Output: True



Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.



Note:

The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.
"""

def is_almost_palindrome(s: str) -> bool:
    def is_palindrome(sub_s: str) -> bool:
        return sub_s == sub_s[::-1]
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Check if removing either the left or right character makes it a palindrome
            return is_palindrome(s[left:right]) or is_palindrome(s[left + 1:right + 1])
        left += 1
        right -= 1
    
    return True