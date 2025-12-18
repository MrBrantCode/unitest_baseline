"""
QUESTION:
Write a function called `checkPalindromeDistinctAlphabets` that takes three parameters: string `s`, string `c`, and integer `n`. The function should return a tuple containing three values: a string that is the result of removing all characters in `s` that are present in `c`, a boolean indicating whether the resulting string is a palindrome, and a boolean indicating whether the resulting string has `n` distinct alphabets.
"""

def checkPalindromeDistinctAlphabets(s, c, n):
    result = ''.join(ch for ch in s if ch not in c)
    palindrome = result == result[::-1]
    num_alphabets = len(set(result))
    
    return result, palindrome, num_alphabets == n