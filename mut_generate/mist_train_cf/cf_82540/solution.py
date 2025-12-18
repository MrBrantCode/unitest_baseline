"""
QUESTION:
Write a function `longest_palindrome(s)` that identifies the longest consecutive palindrome substring from an alphanumeric string input `s`. The function should return the longest palindrome substring. Note that alphanumeric characters are those comprised of the union of the set of all alphabet (A-Z, a-z) and the set of all numbers (0-9). The input string `s` may contain both alphabets and numbers.
"""

def longest_palindrome(s):
    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]

    max_length = 0
    start = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_palindrome(s[i:j]) and j-i > max_length:
                start = i
                max_length = j-i

    return s[start:start+max_length]