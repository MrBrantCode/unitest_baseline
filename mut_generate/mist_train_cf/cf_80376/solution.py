"""
QUESTION:
Create a function named `word_frequency` that takes a text string as input and returns a dictionary where each key is a word from the string and the corresponding value is the frequency of that word. The function should split the string into words at spaces and count the occurrence of each word in a case-sensitive manner.
"""

def word_frequency(str):
    word_dict = {}
    
    # Splitting the string into words
    words = str.split()

    # Counting each word's occurrence
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    
    return word_dict