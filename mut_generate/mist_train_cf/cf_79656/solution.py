"""
QUESTION:
Create a function `detect_palindromes(words, targets)` that detects a specific set of palindromes in a series of disorganized words. The function should take a list of words and a list of target palindromes as input, and return a list of words from the input list that are both palindromes and match the target palindromes (case-insensitive and disregarding non-letter characters). The time complexity of the solution should be at most O(n log n), where n is the total number of letters in all the words combined.
"""

def detect_palindromes(words, targets):
    def remove_nonletters(word):
        return "".join(ch for ch in word if ch.isalpha())

    def is_palindrome(word):
        word = remove_nonletters(word)
        return word.lower() == word[::-1].lower()

    targets = set([target.lower() for target in targets])
    return [word for word in words if remove_nonletters(word).lower() in targets and is_palindrome(word)]