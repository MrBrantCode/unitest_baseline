"""
QUESTION:
Create a function `is_plagiarism(doc1, doc2)` that takes two string documents as input and returns `True` if the documents are identical and `False` otherwise. The function should use the SHA256 hash algorithm to compare the documents. The comparison should be case-sensitive and consider even a single character difference as a non-match.
"""

import hashlib

def is_plagiarism(doc1, doc2):
    """
    This function checks whether two documents are the same based on the hash value 
    resulting from SHA256 algorithm.
    """
    doc1 = doc1.encode('utf-8')
    doc2 = doc2.encode('utf-8')
    return hashlib.sha256(doc1).hexdigest() == hashlib.sha256(doc2).hexdigest()