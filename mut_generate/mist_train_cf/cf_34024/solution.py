"""
QUESTION:
Write a function `find_similar_documents` that takes in a list of documents, an integer `bucket_size`, and a float `minsimilarity`. The function should process the content of the documents using shingling with the given `bucket_size`, calculate the Jaccard similarity score between each pair of documents, and return the pairs of documents that have a similarity score greater than or equal to `minsimilarity`. The function should return a list of tuples, where each tuple contains the indices of the two similar documents (1-indexed).
"""

from typing import List, Tuple
from collections import defaultdict

def shingling(document: str, bucket_size: int) -> set:
    shingles = set()
    words = document.split()
    for i in range(len(words) - bucket_size + 1):
        shingle = " ".join(words[i:i + bucket_size])
        shingles.add(shingle)
    return shingles

def jaccard_similarity(set1: set, set2: set) -> float:
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def find_similar_documents(documents: List[str], bucket_size: int, minsimilarity: float) -> List[Tuple[int, int]]:
    shingle_sets = [shingling(doc, bucket_size) for doc in documents]
    similar_pairs = []
    for i in range(len(documents)):
        for j in range(i + 1, len(documents)):
            similarity = jaccard_similarity(shingle_sets[i], shingle_sets[j])
            if similarity >= minsimilarity:
                similar_pairs.append((i + 1, j + 1))
    return similar_pairs