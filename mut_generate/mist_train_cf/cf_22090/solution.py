"""
QUESTION:
Create a function called `get_longest_palindromes(words)` that takes a list of strings as input and returns the longest palindrome word(s) in the list. A palindrome word is a word that reads the same forwards and backwards. The function should consider words with different capitalization as different words, handle cases where multiple palindrome words have the same maximum length, and return an appropriate message if the input list is empty or contains only empty strings. The time complexity of the function should be O(n), where n is the total number of characters in the input list.
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