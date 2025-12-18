"""
QUESTION:
Create a function `count_words` that takes a comma-separated string as input and returns a dictionary with the frequency of each word's occurrence, excluding words that contain the letter 'e'. Implement this using a single loop and without utilizing built-in functions or libraries for string manipulation or dictionary operations.
"""

def count_words(string):
    word_count = {}
    current_word = ""
    word_started = False
    
    for char in string:
        if char == ',':
            if current_word and 'e' not in current_word:
                word_count[current_word] = word_count.get(current_word, 0) + 1
            current_word = ""
            word_started = False
        elif char != ' ':
            if not word_started:
                word_started = True
            current_word += char
    
    if current_word and 'e' not in current_word:
        word_count[current_word] = word_count.get(current_word, 0) + 1
    
    return word_count