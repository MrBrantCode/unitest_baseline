"""
QUESTION:
Create a function called `find_palindrome_substrings` that takes a string as input and returns a tuple containing a list of all distinct palindromic substrings and their total count. The function should consider a string as a substring and a palindrome of itself.
"""

from typing import List, Tuple

def find_palindrome_substrings(string: str) -> Tuple[List[str], int]:
    substrings = set(string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1))
    palindromes = [s for s in substrings if s == s[::-1]]
    return palindromes, len(palindromes)