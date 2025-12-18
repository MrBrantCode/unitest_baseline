"""
QUESTION:
Write a function `isPalindrome(s)` that checks if the input string `s` is a palindrome. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), using no extra space.
"""

def isPalindrome(s):
    i = 0
    j = len(s) - 1
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True