"""
QUESTION:
Write a function `is_palindrome` that checks if an input string is a palindrome. The function should ignore case sensitivity, special characters, numbers, and spaces. It should have a time complexity of O(n), where n is the length of the input string. The input string may contain uppercase and lowercase letters, numbers, special characters, and spaces, and will have at most length 10^5.
"""

def is_palindrome(s):
    s = s.lower()  
    start = 0
    end = len(s) - 1
    
    while start < end:
        # Ignore special characters, numbers, and spaces
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1
            
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1
        
    return True