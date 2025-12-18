"""
QUESTION:
Design a function `is_palindrome` that takes a string as input and returns True if the string is a palindrome (ignoring non-alphanumeric characters, case, and whitespaces) and False otherwise. Additionally, design a function `is_palindrome_number` that takes an integer as input and returns True if the integer is a palindrome and False otherwise.
"""

def is_palindrome(s):
    s = s.lower()
    start, end = 0, len(s) - 1

    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1

        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True

def is_palindrome_number(n):
    num_str = str(n)
    start, end = 0, len(num_str) - 1
    
    while start < end:
        if num_str[start] != num_str[end]:
            return False
        start += 1
        end -= 1

    return True