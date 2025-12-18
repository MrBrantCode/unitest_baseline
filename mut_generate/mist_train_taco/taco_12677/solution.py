"""
QUESTION:
Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.
After doing so, return the final string.  If there is no way to do so, return the empty string.
 
Example 1:
Input: palindrome = "abccba"
Output: "aaccba"

Example 2:
Input: palindrome = "a"
Output: ""

 
Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""

def break_palindrome(palindrome: str) -> str:
    if len(palindrome) == 1:
        return ''
    
    for i, char in enumerate(palindrome):
        if char != 'a' and i != len(palindrome) // 2:
            return palindrome[:i] + 'a' + palindrome[i + 1:]
        elif char == 'a' and i == len(palindrome) - 1:
            return palindrome[:-1] + 'b'
    
    return ''