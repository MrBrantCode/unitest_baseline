"""
QUESTION:
Write a function `find_palindrome_pairs` that takes a list of words as input and returns all unique pairs of index values (i, j) such that the concatenation of the words at indices i and j forms a palindrome. The function should not return duplicate pairs, i.e., if (i, j) is a valid pair, (j, i) should not be included in the result.
"""

def find_palindrome_pairs(words):
    """
    Returns all unique pairs of index values (i, j) 
    such that the concatenation of the words at indices i and j forms a palindrome.

    Args:
    words (list): A list of words.

    Returns:
    list: A list of tuples, where each tuple contains a pair of indices (i, j) 
          that form a palindrome when concatenated.
    """
    
    def is_palindrome(word):
        """
        Checks if a word is a palindrome.

        Args:
        word (str): The word to check.

        Returns:
        bool: True if the word is a palindrome, False otherwise.
        """
        return word == word[::-1]

    result = []
    n = len(words)

    for i in range(n):
        for j in range(i + 1, n):
            if is_palindrome(words[i] + words[j]):
                result.append((i, j))
            if is_palindrome(words[j] + words[i]):
                result.append((j, i))

    return result