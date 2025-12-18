"""
QUESTION:
Write a function `palindrome_pairs` that takes a list of words as input and returns all pairs of distinct indices (i, j) such that the concatenation of the two words at these indices is a palindrome. The function should handle words containing non-alphabetic characters and should ignore case.
"""

def palindrome_pairs(words):
    def is_palindrome(word):
        # Helper function to check if a word is a palindrome
        word = ''.join(ch for ch in word if ch.isalnum()).lower()
        return word == word[::-1]

    result = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_palindrome(words[i] + words[j]):
                result.append((i, j))
            if is_palindrome(words[j] + words[i]):
                result.append((j, i))
    return result