"""
QUESTION:
Implement a function named `find_all_longest_palindromes` that takes a string `s` as input and returns all the longest palindromic substrings, disregarding white spaces, punctuation, and case sensitivity. The function should handle large text inputs efficiently.
"""

def find_all_longest_palindromes(s):
    s = s.lower()
    s = ''.join([c for c in s if c.isalnum()])

    n = len(s)
    dp = [[False]*n for _ in range(n)]
    longest_length = 0
    longest_palindromes = []
    
    for l in range(n):
        for i in range(n-l):
            j = i+l
            if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                dp[i][j] = True
                if longest_length < l+1:
                    longest_length = l+1
                    longest_palindromes = [s[i:j+1]]
                elif longest_length == l+1:
                    longest_palindromes.append(s[i:j+1])
                    
    return longest_palindromes