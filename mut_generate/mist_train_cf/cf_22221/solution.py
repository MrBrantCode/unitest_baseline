"""
QUESTION:
Write a function named `find_word_occurrences` that takes a string `s` and a list of words `words` as input, and returns a dictionary containing the frequency of each word in `s`. The string `s` contains lowercase letters and no punctuation or special characters, and each word in `s` is separated by a single space. Each word in `words` consists of lowercase letters and has a length between 1 and 20 characters. The function should ignore any occurrences of words that are part of a larger word in `s`.
"""

def find_word_occurrences(s, words):
    occurrences = {}
    words_in_string = s.split()
    
    for word in words:
        count = 0
        for string_word in words_in_string:
            if string_word.find(word) >= 0 and len(string_word) == len(word):
                count += 1
        occurrences[word] = count
    
    return occurrences