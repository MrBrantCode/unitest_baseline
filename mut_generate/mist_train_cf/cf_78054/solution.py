"""
QUESTION:
Given two sentences A and B, each consisting of lowercase alphabets and spaces, with a maximum length of 200 characters, write a function `uncommonFromSentences(A: str, B: str)` that returns a list of uncommon words, where an uncommon word is a word that appears in only one of the sentences.
"""

from collections import Counter

def uncommonFromSentences(A: str, B: str):
    A_counts = Counter(A.split())
    B_counts = Counter(B.split())
    
    return [word for word in A_counts if A_counts[word] == 1 and word not in B_counts] + [word for word in B_counts if B_counts[word] == 1 and word not in A_counts]