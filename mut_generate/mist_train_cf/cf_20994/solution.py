"""
QUESTION:
Write a function `longest_palindrome_substring` that finds the longest substring of four characters in a given string that is a palindrome. The substring should read the same backward as forward and have a length of four characters.
"""

def longest_palindrome_substring(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    max_length = 4
    max_palindrome = ""
    
    for i in range(len(s) - max_length + 1):
        for j in range(i + max_length, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub) and len(sub) > len(max_palindrome):
                max_palindrome = sub
                
    return max_palindrome if len(max_palindrome) == max_length else ""