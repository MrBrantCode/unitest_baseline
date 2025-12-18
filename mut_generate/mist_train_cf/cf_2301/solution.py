"""
QUESTION:
Write a function named `count_word_occurrences` that takes two parameters: `sentence` and `word`. The function should return the number of occurrences of `word` in `sentence` in a case-insensitive manner, ignoring any punctuation marks and special characters within the words.
"""

def count_word_occurrences(sentence, word):
    sentence = sentence.lower()
    word = word.lower()
    
    count = 0
    words = sentence.split()
    
    for word_in_sentence in words:
        cleaned_word = ''.join(c for c in word_in_sentence if c.isalnum())
        
        if cleaned_word == word:
            count += 1
    
    return count