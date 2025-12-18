"""
QUESTION:
Create a function named `count_unique_words` that takes a string of unlimited length as input. The function should return the number of unique words in the string, considering case sensitivity and punctuation marks. Common stopwords in the English language should be ignored, and words with different capitalization or followed by punctuation marks should be treated as different words.
"""

def count_unique_words(string):
    stopwords = ['the', 'and', 'a', 'an', 'is', 'in', 'it', 'of', 'to', 'for', 'with', 'on', 'at', 'by', 'from']
    
    unique_words = set()
    words = string.split()

    for word in words:
        if word.lower() in stopwords:
            continue
        if not word.strip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ').isalpha():
            unique_words.add(word.lower())
        else:
            unique_words.add(word)
    
    return len(unique_words)