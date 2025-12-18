"""
QUESTION:
Write a function `is_palindrome` that checks if a given string is a palindrome, ignoring non-alphabetic characters and letter casing. The function should return a tuple containing a boolean value indicating whether the string is a palindrome and the longest palindrome substring found in the string. The returned substring should be in lowercase.
"""

def is_palindrome(s):
    clean_str = ''
    s = s.lower()
    for char in s:
        if char.isalpha():
            clean_str += char
    start = 0
    end = 0
    max_len = 0
    for i in range(len(clean_str)):
        for j in range(len(clean_str), i, -1):
            substr = clean_str[i:j]
            if substr == substr[::-1] and len(substr) > max_len:
                max_len = len(substr)
                start = i
                end = j
    return (clean_str == clean_str[::-1], clean_str[start:end])