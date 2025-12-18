"""
QUESTION:
Write a function named `find_unrelated_word` that determines the word in the third sentence of a given paragraph that is not related to the others. The function should take a paragraph as input and return the unrelated word. Assume the paragraph contains at least three sentences. The word is considered unrelated if it is not in a predefined set of related words {"birds", "singing", "sweet", "melodies", "filling", "air", "joy", "peacefulness", "moment"}.
"""

def find_unrelated_word(paragraph):
    sentences = paragraph.split(". ")  # split the paragraph into sentences
    words = sentences[2].split()  # split the third sentence into words
    related_words = {"birds", "singing", "sweet", "melodies", "filling", "air", "joy", "peacefulness", "moment"}  # create a set of related words
    unrelated_word = ""
    for word in words:
        if word.lower() not in related_words:
            unrelated_word = word
            break
    return unrelated_word