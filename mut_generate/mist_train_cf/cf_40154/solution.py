"""
QUESTION:
Implement a function named `evaluate_clusters` that takes two sets of documents, `gold_documents` and `auto_documents`, as input. The function should compare the clustering results of the two sets and return the evaluation result. Additionally, calculate the purity coefficient (pc) for a specific cluster (c) using a 2x2 confusion matrix. The function should be implemented based on a specific clustering evaluation method, such as the Jaccard index, Rand index, etc. The output of the function should be used to calculate the purity coefficient (pc) as pc = confusion[c, c] / (confusion[c, c] + confusion[n, c]).
"""

def evaluate_clusters(gold_documents, auto_documents):
    intersection = len(set(gold_documents) & set(auto_documents))
    union = len(set(gold_documents) | set(auto_documents))
    jaccard_index = intersection / union
    return jaccard_index