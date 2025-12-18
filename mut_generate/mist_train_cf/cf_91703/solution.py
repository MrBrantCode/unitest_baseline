"""
QUESTION:
Write a function `palindrome_pairs` that takes a list of words as input and returns all pairs of distinct indices (i, j) in the list such that the concatenation of the words at these indices, i.e., `words[i] + words[j]`, is a palindrome. The function should handle cases where the words are not necessarily lowercase alphabetic characters and may contain punctuation and whitespace.
"""

def palindrome_pairs(words):
    def is_palindrome(word):
        word = ''.join(ch for ch in word if ch.isalnum()).lower()
        return word == word[::-1]

    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and is_palindrome(words[i] + words[j]):
                result.append((i, j))
    return result