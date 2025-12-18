"""
QUESTION:
Write a Python function `find_unrelated_word` that takes a paragraph and a set of related words as input, splits the paragraph into sentences, identifies the third sentence, and returns the word in that sentence that is not related to the others in the sentence. The function should only consider words in the third sentence and the set of related words, ignoring any punctuation and case sensitivity.
"""

def find_unrelated_word(paragraph, related_words):
    """
    This function takes a paragraph and a set of related words, 
    splits the paragraph into sentences, identifies the third sentence, 
    and returns the word in that sentence that is not related to the others in the sentence.

    Args:
        paragraph (str): A string of sentences.
        related_words (set): A set of related words.

    Returns:
        str: The unrelated word in the third sentence.
    """
    sentences = paragraph.split(". ")  # split the paragraph into sentences
    words = sentences[2].lower().split()  # split the third sentence into words
    unrelated_word = ""
    for word in words:
        word = ''.join(e for e in word if e.isalnum())  # remove punctuation
        if word not in related_words:
            unrelated_word = word
            break
    return unrelated_word