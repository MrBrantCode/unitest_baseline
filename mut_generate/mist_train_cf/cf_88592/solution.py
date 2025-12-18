"""
QUESTION:
Create a function named `count_words` that takes a string of words and an optional language parameter as input. The function should return a dictionary with the count of each word, excluding common stop words for the specified language. The function should be case insensitive, handle punctuation marks and special characters, and support compound words. The function should be efficient enough to handle very large input strings.

The function should ignore case sensitivity, exclude common English stop words such as "a", "an", "the", "is", "of", etc., and handle punctuation marks and special characters properly. The function should also identify and count compound words, which are formed by combining two or more words. The function should support multiple languages, allowing the user to specify the language of the input text. The stop words and language-specific rules for handling punctuation should be applied accordingly.
"""

import re
from collections import defaultdict

def count_words(word_string, language='english'):
    stop_words = get_stop_words(language)
    word_counts = defaultdict(int)
    compound_words = []
    
    # Remove punctuation marks and special characters
    word_string = re.sub(r'[^\w\s]', '', word_string)
    
    # Split the string into individual words
    words = word_string.lower().split()
    
    # Check if each word is a stop word or a compound word
    for word in words:
        if word not in stop_words:
            if ' ' in word:
                compound_words.append(word)
            else:
                word_counts[word] += 1
    
    # Count the compound words
    for compound_word in compound_words:
        word_counts[compound_word] += 1
    
    return word_counts

def get_stop_words(language):
    # Implement logic to return stop words based on the specified language
    # You can use a pre-defined list of stop words for each language, or use a library like NLTK to fetch stop words
    
    stop_words = set()
    
    if language == 'english':
        stop_words = {'a', 'an', 'the', 'is', 'of', 'in'}
    
    # Add stop words for other languages as needed
    
    return stop_words