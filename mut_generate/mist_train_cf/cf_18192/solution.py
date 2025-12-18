"""
QUESTION:
Write a function `sort_words` that takes a list of words as input. Sort the list alphabetically in descending order, ignoring case sensitivity, and remove any duplicate words. The function should only use built-in functions and not rely on external libraries or modules.
"""

def sort_words(words):
    # Convert all words to lowercase for case-insensitive sorting
    words = [word.lower() for word in words]
    
    # Remove duplicate words
    words = list(set(words))
    
    # Sort words in descending order
    words.sort(reverse=True)
    
    return words