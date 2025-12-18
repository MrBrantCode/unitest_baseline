"""
QUESTION:
Create a function `get_longest_palindromes` that returns the longest palindrome word(s) from a given list of strings. The function should consider different capitalization as distinct words, handle empty input lists or lists containing only empty strings, and return all palindrome words with the same maximum length. The function should have a time complexity of O(n), where n is the total number of characters in the input list.
"""

def get_longest_palindromes(words):
    if not words or all(word == "" for word in words):
        return "Input list is empty or contains only empty strings."
    
    longest_length = 0
    longest_palindromes = []
    
    for word in words:
        word_length = len(word)
        if word == word[::-1] and word_length >= longest_length:
            if word_length > longest_length:
                longest_palindromes = []
                longest_length = word_length
            longest_palindromes.append(word)
    
    if not longest_palindromes:
        return "No palindrome words found in the list."
    return longest_palindromes