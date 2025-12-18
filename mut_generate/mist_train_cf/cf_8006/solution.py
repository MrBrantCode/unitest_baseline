"""
QUESTION:
Create a function named `sort_dictionary` that takes a dictionary `word_freq` as an argument. The function should sort the dictionary in descending order based on the word frequencies, ignoring any words that contain special characters or numbers, and removing any words that have a frequency less than or equal to 10. The function should handle cases where the words contain accented characters or are written in different character encodings, and should be able to handle words written in different languages.
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