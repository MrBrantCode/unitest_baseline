"""
QUESTION:
Write a function `find_palindrome_pairs(words)` that finds all pairs of distinct indices `(i, j)` in the given list of strings `words`, such that the concatenation of the two strings `words[i] + words[j]` is a palindrome. The function should consider all possible pairs of distinct indices `(i, j)` in the given list and check if the concatenation is a palindrome in both forward and backward directions. The function should return all pairs of distinct indices `(i, j)` where the concatenation is a palindrome.
"""

def find_palindrome_pairs(words):
    """
    Finds all pairs of distinct indices (i, j) in the given list of strings `words`, 
    such that the concatenation of the two strings `words[i] + words[j]` is a palindrome.

    Args:
    words (list): A list of strings.

    Returns:
    list: A list of pairs of distinct indices (i, j) where the concatenation is a palindrome.
    """
    def is_palindrome(s):
        # Function to check if a string is a palindrome
        return s == s[::-1]

    pairs = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                concat = words[i] + words[j]
                if is_palindrome(concat):
                    pairs.append((i, j))
    return pairs