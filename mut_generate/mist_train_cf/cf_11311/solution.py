"""
QUESTION:
Create a function named 'is_substring' that takes two strings s1 and s2 as input. The function should check if s2 is a substring of s1 and return True if it is, False otherwise. The function should be case-sensitive, ignore leading and trailing whitespaces in both strings, and handle empty strings as inputs by returning False. The function should also handle special characters and numbers in both strings by ignoring them during the substring check.
"""

def is_substring(s1, s2):
    s1 = s1.strip()
    s2 = s2.strip()
    
    if s1 == "" or s2 == "":
        return False
    
    s1 = ''.join(e for e in s1 if e.isalnum())
    s2 = ''.join(e for e in s2 if e.isalnum())
    
    return s2 in s1