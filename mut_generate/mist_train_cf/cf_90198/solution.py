"""
QUESTION:
Create a function named `sort_dictionary` that takes a dictionary `word_freq` as an argument, where the keys are words and the values are their frequencies. The function should sort the dictionary in descending order based on the word frequencies, removing any words with frequencies less than or equal to 10 and ignoring any words that contain special characters or numbers. The function should be able to handle words with accented characters and words written in different languages and character encodings.
"""

import unicodedata

def sort_dictionary(word_freq):
    sorted_words = []
    
    for word, freq in word_freq.items():
        if freq > 10 and word.isalpha():
            normalized_word = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode()
            sorted_words.append((normalized_word, freq))
    
    sorted_words.sort(key=lambda x: x[1], reverse=True)
    
    return sorted_words