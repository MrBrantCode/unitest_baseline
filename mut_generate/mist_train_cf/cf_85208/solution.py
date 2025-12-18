"""
QUESTION:
Write a function `count_palindromes(s)` that takes a string `s` of length `N` and returns the count of all unique palindromic substrings in the string. The function should also print out these unique palindromic substrings. The time complexity of the function should be O(n^2) or better, and it should avoid counting duplicate palindromic substrings.
"""

def count_palindromes(s):

    N = len(s)
    palindromes = set()

    for center in range(2*N - 1):
        left = center // 2
        right = left + center % 2

        while left >= 0 and right < N and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left = left - 1
            right = right + 1

    print(palindromes)

    return len(palindromes)