"""
QUESTION:
Write a function `find_word_occurrences` that takes a string `s` and a list of words `words` as input. The function should return a dictionary where each key is a word from the `words` list and its corresponding value is the frequency of that word in the string `s`. The string `s` contains lowercase letters only, is separated by spaces, and has no punctuation marks or special characters. The `words` list contains at most 100 lowercase words, each with a length between 1 and 20 characters. A word in `s` should be considered a separate occurrence only if it is not part of a larger word.
"""

def find_word_occurrences(s, words):
    occurrences = {}
    words_in_string = s.split()
    
    for word in words:
        count = 0
        for string_word in words_in_string:
            if string_word == word:
                count += 1
        occurrences[word] = count
    
    return occurrences