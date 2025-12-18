"""
QUESTION:
Write a function called `longest_palindrome_words` that returns the longest palindrome word(s) in a given list of strings. The function should consider words with different capitalization as different words, handle cases where multiple palindrome words have the same maximum length, and return an appropriate message for an empty input list or a list with no palindrome words. The function should have a time complexity of O(n^2), where n is the total number of characters in the input list.
"""

def longest_palindrome_words(words):
    if not words:
        return "The input list is empty."
    
    longest_words = []
    max_length = 0
    
    for word in words:
        if word == word[::-1]:
            if len(word) > max_length:
                longest_words = [word]
                max_length = len(word)
            elif len(word) == max_length:
                longest_words.append(word)
    
    if not longest_words:
        return "No palindrome words found in the input list."
    
    return longest_words