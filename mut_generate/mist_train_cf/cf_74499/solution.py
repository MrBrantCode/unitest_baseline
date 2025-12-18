"""
QUESTION:
Write a function `count_letters_and_words(text)` that takes a string of text as input and returns two dictionaries: one for the count of each letter (case insensitive) and one for the count of each word (case sensitive), ignoring punctuation marks.
"""

def count_letters_and_words(text):
    letter_count = {}
    word_count = {}

    # removing punctuation
    text_no_punctuation = "".join(c for c in text if c not in ('!', '.', ':', ',', ';', '?'))
    
    for letter in text_no_punctuation.lower():
        if letter != ' ':
            letter_count[letter] = letter_count.get(letter, 0) + 1
    
    for word in text_no_punctuation.split():
        word_count[word] = word_count.get(word, 0) + 1
        
    return letter_count, word_count