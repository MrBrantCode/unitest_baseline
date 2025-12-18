"""
QUESTION:
Create a function named `check_palindrome` that takes a list of strings as input. The function should return a list of tuples, where each tuple contains a boolean value indicating whether the corresponding input string is a palindrome (ignoring non-alphabetic characters and case) and the longest palindrome substring found in the string (in lowercase). The longest palindrome substring should be the longest sequence of characters that reads the same forward and backward.
"""

def check_palindrome(strings):
    def is_palindrome(string):
        string = ''.join(c.lower() for c in string if c.isalpha())
        return string == string[::-1]

    def longest_palindrome_substring(string):
        string = ''.join(c.lower() for c in string if c.isalpha())
        longest_substring = ""
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                substring = string[i:j]
                if is_palindrome(substring) and len(substring) > len(longest_substring):
                    longest_substring = substring
        return longest_substring

    return [(is_palindrome(s), longest_palindrome_substring(s)) for s in strings]