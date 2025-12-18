"""
QUESTION:
Write a function `search_word(string, word)` that searches for a word in a given string, ignoring case sensitivity, and returns a list of the starting index positions of all occurrences of the word.
"""

def search_word(string, word):
    string = string.lower()
    word = word.lower()
    
    positions = []
    start = 0
    while start < len(string):
        index = string.find(word, start)
        if index == -1:
            break
        positions.append(index)
        start = index + len(word)
    
    return positions