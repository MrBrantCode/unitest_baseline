"""
QUESTION:
Write a function `find_largest_common_palindrome(arr)` that takes an array of strings as input and returns the largest common palindromic substring among them. The substring must appear in at least half of the strings in the array. If no such substring exists, return None.
"""

def is_palindrome(s):
    return s == s[::-1]

def find_substrings(s):
    n = len(s)
    return [s[i:j+1] for i in range(n) for j in range(i, n)]

def find_largest_common_palindrome(arr):
    palindromes = {}
    for s in arr:
        substrings = find_substrings(s)
        for sub in substrings:
            if is_palindrome(sub):
                if sub in palindromes:
                    palindromes[sub] += 1
                else:
                    palindromes[sub] = 1
    half_len = len(arr) // 2
    candidates = [p for p in palindromes if palindromes[p] >= half_len]
    if not candidates:
        return None
    return max(candidates, key=len)