"""
QUESTION:
Write a function called `find_palindromes` that takes a list of strings as input and returns a list of all the palindromes in the input list, sorted in ascending order by length. If the input list does not contain any palindromes, return an empty list.
"""

def find_palindromes(words):
    palindromes = [word for word in words if word == word[::-1]]
    return sorted(palindromes, key=len)