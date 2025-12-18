"""
QUESTION:
Write a function `count_words_in_string` that takes a string `string` and a list of words `word_list` as input. The function should count the number of unique words from `word_list` that appear in `string`, considering case sensitivity and punctuation. The function should not count repetitions of the same word.
"""

def count_words_in_string(string, word_list):
    import string as str_module
    
    string = string.translate(str.maketrans('', '', str_module.punctuation))
    
    string = string.lower()
    
    counter = 0
    for word in word_list:
        if string.find(word.lower()) != -1:
            counter += 1
            
    return counter