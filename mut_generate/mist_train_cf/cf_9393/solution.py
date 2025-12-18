"""
QUESTION:
Write a function called `search_word` that takes two parameters: `string` and `word`. The function should search for the `word` in the `string` ignoring case sensitivity and return a list of the starting index positions of each occurrence of the `word`.
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