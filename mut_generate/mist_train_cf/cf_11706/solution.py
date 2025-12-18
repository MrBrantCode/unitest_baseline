"""
QUESTION:
Write a function called `is_palindrome` that checks if a given string is a palindrome while ignoring all non-alphabetic characters and considering the string case-insensitive. The function should have a time complexity of O(n) and should not use any built-in functions or libraries for string manipulation, except for checking if a character is alphabetic. The function should return a boolean value indicating whether the string is a palindrome or not.
"""

def is_palindrome(string):
    start = 0
    end = len(string) - 1
    string = string.lower()
    
    while start < end:
        if not string[start].isalpha():
            start += 1
            continue
        if not string[end].isalpha():
            end -= 1
            continue
        
        if string[start] != string[end]:
            return False
        
        start += 1
        end -= 1
    
    return True