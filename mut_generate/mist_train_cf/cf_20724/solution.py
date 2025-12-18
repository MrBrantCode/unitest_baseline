"""
QUESTION:
Implement a function `remove_duplicates(sentence)` that takes a string of alphanumeric characters and spaces as input. The function should remove all duplicate words from the sentence while preserving the order of the remaining words. The solution should have a time complexity of O(n), where n is the length of the sentence. The implementation should use a single loop and not utilize any built-in functions or data structures to store unique words. String manipulation or comparison operations should also not be used within the loop.
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