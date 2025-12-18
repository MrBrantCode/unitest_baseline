"""
QUESTION:
Create an algorithm with the function name `sort_words` that takes a list of words as input and returns a list of words sorted in alphabetical order without duplicates. The function should be case-insensitive and handle both uppercase and lowercase letters. The function should not use any built-in sorting functions.
"""

def sort_words(words):
    words = [word.lower() for word in words]
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    sorted_array = []
    
    for word, freq in sorted(word_freq.items()):
        sorted_array.extend([word] * freq)
    
    return sorted_array