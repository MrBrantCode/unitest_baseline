"""
QUESTION:
Write a function `find_word_occurrences` that takes a string `s` and a list of words `words` as input, and returns a dictionary containing the frequency of each word in `s`, ignoring occurrences that are part of a larger word. The string `s` contains only lowercase letters and words separated by single spaces, and the list `words` contains at most 100 words with lengths between 1 and 20 characters. The function should have a time complexity of O(n), where n is the length of the string `s`.
"""

def find_word_occurrences(s, words):
    word_counts = {}
    for word in words:
        word_counts[word] = 0
        
    words_in_s = s.split()
    for word in words_in_s:
        if word in words:
            word_counts[word] += 1
            
    return word_counts