"""
QUESTION:
Write a function `most_common_words` that takes a sentence as input and returns a list of the three most frequent words in the sentence. The function should ignore punctuation and be case-insensitive.
"""

import string

def most_common_words(sentence):
    # Remove punctuation and convert to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split sentence into words
    words = sentence.split()
    
    # Count occurrences of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort words by frequency and return the top three
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return [word[0] for word in sorted_words[:3]]