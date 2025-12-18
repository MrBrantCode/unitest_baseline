"""
QUESTION:
Design a recursive function named `word_traversal` that takes a list of words and optional parameters `wordIndex` (default 0) and `letterIndex` (default 0) as input. The function should print each letter of all the words on a separate line, keeping track of the index of each letter in its corresponding word and the index of each word in the list. The function should handle edge cases, including an empty list and non-string elements.
"""

def word_traversal(wordList, wordIndex=0, letterIndex=0):
    # Check for empty list or end of list
    if not wordList or wordIndex >= len(wordList):
        return
    
    word = wordList[wordIndex]
    
    # Handle non-string elements
    if not isinstance(word, str):
        word_traversal(wordList, wordIndex + 1, 0)
        return

    # Check for end of word
    if letterIndex >= len(word):
        word_traversal(wordList, wordIndex + 1, 0)
    else:
        print(f'Word {wordIndex + 1}, Letter {letterIndex + 1}: {word[letterIndex]}')
        word_traversal(wordList, wordIndex, letterIndex + 1)