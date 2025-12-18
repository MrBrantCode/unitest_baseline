"""
QUESTION:
Create a function `compare_docs(doc1, doc2)` that takes two documents as strings, compares them, and returns the count of unique words present in both documents and the frequency of each of those words across the documents. The comparison should ignore case-sensitivity and punctuation. The function should be optimized for efficiency to handle large documents containing any Unicode characters.
"""

import collections
import string

def compare_docs(doc1, doc2):
    # clean and count words in both documents
    doc1_words = collections.Counter(doc1.translate(str.maketrans('', '', string.punctuation)).lower().split())
    doc2_words = collections.Counter(doc2.translate(str.maketrans('', '', string.punctuation)).lower().split())

    # find unique words common to both documents
    common_words = set(doc1_words.keys()) & set(doc2_words.keys())

    return len(common_words), {word: (doc1_words[word], doc2_words[word]) for word in common_words}