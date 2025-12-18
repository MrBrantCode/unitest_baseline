"""
QUESTION:
Write a function called `find_words_with_letter` that takes a list of words and a specific letter as input, and returns a list of words that contain the specific letter, regardless of the case of the letter or the word. The function should be case-insensitive.
"""

def find_words_with_letter(words, letter):
    result = []
    for word in words:
        if letter.lower() in word.lower():
            result.append(word)
    return result