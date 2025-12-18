"""
QUESTION:
Design a function `filter_words(words, chars)` that filters a list of words based on the presence of characters in a given string, ignoring case sensitivity and handling special characters. The function should return a list of words that contain at least one character from the given string, with no duplicates.
"""

def filter_words(words, chars):
    result = []
    for word in words:
        for i in chars:
            if i in word.lower():
                if word not in result:
                    result.append(word)
                break
    return result