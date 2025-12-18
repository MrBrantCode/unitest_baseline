"""
QUESTION:
Write a function `longestPalindrome` that takes a string `st` as input and returns the longest palindrome substring in `st`. A palindrome is a string that reads the same backward as forward, ignoring case, spaces, and punctuation. The function should return the longest palindrome found, or the shortest palindrome if there are multiple palindromes of the same maximum length.
"""

def longestPalindrome(st): 
    st = ''.join(e for e in st if e.isalnum()).lower()
    palindromes = []
    for i in range(len(st)): 
        for j in range(i, len(st)): 
            curr = st[i:j+1] 
            rev = curr[::-1] 
            if (curr == rev): 
                palindromes.append(curr) 
    if palindromes:
        return max(palindromes, key = len)
    else:
        return ""