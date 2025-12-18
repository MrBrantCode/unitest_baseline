"""
QUESTION:
Write two functions, `find_char(words, target_char)` and `count_char(words, target_char)`, to find and count a distinct alphabetic symbol within a collection of words. The `find_char` function should return a list of words containing the target character, and the `count_char` function should return the total number of times the target character appears in the list of words.
"""

def find_and_count_char(words, target_char):
    found_words = [word for word in words if target_char in word]
    char_count = sum(word.count(target_char) for word in words)
    return found_words, char_count