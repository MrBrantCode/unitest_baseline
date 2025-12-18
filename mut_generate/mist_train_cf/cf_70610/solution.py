"""
QUESTION:
Write a function named `longest_word` that takes two parameters: a list of alphabetical symbols and a list of words. The function should return the longest word that can be formed using the given alphabetical symbols. If no such word is found, return an empty string.
"""

def longest_word(symbols, words):
    symbols_set = set(symbols)
    words.sort(key=len, reverse=True)
  
    for word in words:
        if set(word).issubset(symbols_set):
            return word
    return ""