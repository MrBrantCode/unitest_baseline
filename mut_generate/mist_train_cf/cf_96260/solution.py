"""
QUESTION:
Implement a function called `remove_duplicates` that takes a string of alphanumeric characters and spaces as input, removes all duplicate words while preserving the order of the remaining words, and returns the resulting string. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in functions or data structures to store unique words, string manipulation, or comparison operations within a single loop.
"""

def remove_duplicates(sentence):
    words = ""
    unique_words = ""
    word_start = 0
    word_end = 0
    sentence_length = len(sentence)
    
    while word_end < sentence_length:
        if sentence[word_end] == " ":
            current_word = sentence[word_start:word_end]
            if current_word not in words:
                words += current_word + " "
                unique_words += current_word + " "
            word_start = word_end + 1
        word_end += 1
    
    # Check the last word in the sentence
    current_word = sentence[word_start:word_end]
    if current_word not in words:
        unique_words += current_word
    
    return unique_words.strip()