"""
QUESTION:
Create a function `check_word_anagram(word, doc)` that takes a word and a document as input and returns a boolean indicating whether the document contains an anagram of the word. The search should be case-insensitive, and only alphabetic characters should be considered. The function should return True if the document contains the anagram of the word and False otherwise.
"""

def check_word_anagram(word, doc):
    word_freq_dict = {}
    for c in word.lower():
        if c.isalpha():
            if c in word_freq_dict:
                word_freq_dict[c] += 1
            else:
                word_freq_dict[c] = 1
                
    doc_freq_dict = {}
    for c in doc.lower():
        if c.isalpha():
            if c in doc_freq_dict:
                doc_freq_dict[c] += 1
            else:
                doc_freq_dict[c] = 1
                
    for key in word_freq_dict:
        if key not in doc_freq_dict or word_freq_dict[key] > doc_freq_dict[key]:
            return False
    return True