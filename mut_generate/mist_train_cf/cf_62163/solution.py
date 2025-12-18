"""
QUESTION:
Write a function named `count_palindrome_substrings` that takes a string as input and returns the number of unique palindromic substrings present in the string. The function should consider single-character substrings as palindromes and substrings should not be repeated in the count.
"""

def count_palindrome_substrings(string: str) -> int:
    n = len(string)
    palindrome_counter = 0
    palindromes_found = set()

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    for i in range(n):
        for j in range(i+1, n+1):
            current_substring = string[i:j]
            if current_substring not in palindromes_found and is_palindrome(current_substring):
                palindrome_counter += 1
                palindromes_found.add(current_substring)

    return palindrome_counter