"""
QUESTION:
Create a function called `find_palindromes` that takes a string `s` as input and returns a list of all substrings in `s` that are palindromes, including single-character substrings.
"""

def find_palindromes(s):
    palindromes = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.append(substr)
    return palindromes