"""
QUESTION:
Create a function named `count_palindromes` that takes a string `s` as input and returns the total count of all palindromic substrings in the string. A palindromic substring is a substring that reads the same backwards as forwards. The function should include single characters as palindromic substrings.
"""

def count_palindromes(s: str) -> int:
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):  
            if s[i:j] == s[i:j][::-1]:  
                count += 1
    return count