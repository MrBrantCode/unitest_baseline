"""
QUESTION:
Design a function `count_word_occurrences(sentence, word)` that counts the number of times a word occurs in a sentence. The function should be case-insensitive and consider punctuation marks and special characters as part of the word. The function takes two parameters: a string `sentence` and a string `word`, and returns the number of occurrences of `word` in `sentence`.
"""

def count_word_occurrences(sentence, word):
    count = 0
    sentence_lower = sentence.lower()
    word_lower = word.lower()
    words = sentence_lower.split()
    
    for w in words:
        clean_word = ''.join(e for e in w if e.isalnum())
        if clean_word == word_lower:
            count += 1
    
    return count