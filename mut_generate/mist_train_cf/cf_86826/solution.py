"""
QUESTION:
Create a function called `isPalindrome` that takes a string `s` as input and returns a boolean value. The function should check if the input string is a palindrome, ignoring special characters and considering case sensitivity, with a time complexity of O(n) and space complexity of O(n).
"""

def entance(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True