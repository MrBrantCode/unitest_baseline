"""
QUESTION:
Write a function find_max that accepts a list of unique strings and an optional boolean parameter case_sensitive. The function should return the string with the highest number of unique characters. If case_sensitive is False (default), disregard the difference in textual casing; otherwise, differentiate between upper and lower case characters. In case of a tie, return the word that comes first lexicographically.
"""

def find_max(words, case_sensitive=False):
    max_unique_count = 0
    max_unique_word = None
    
    for word in sorted(words):
        temp_word = word
        if not case_sensitive:
            temp_word = word.lower()
        unique_char_count = len(set(temp_word))
        if unique_char_count > max_unique_count:
            max_unique_count = unique_char_count
            max_unique_word = word
    return max_unique_word