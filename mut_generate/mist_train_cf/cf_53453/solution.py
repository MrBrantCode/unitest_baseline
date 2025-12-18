"""
QUESTION:
Create a function `average_lemma_embeddings` that takes a dictionary of lemmas with their corresponding embeddings as input and returns a dictionary with averaged embeddings for each lemma. Assume that each lemma has multiple embeddings due to different conjugations or instances in a corpus. The function should average the embeddings to get a decent approximation for a generic context-independent representation of the lemma.
"""

def average_lemma_embeddings(lemmas_embeddings):
    """
    This function calculates the average embeddings for each lemma in a given dictionary.

    Args:
        lemmas_embeddings (dict): A dictionary where keys are lemmas and values are lists of their corresponding embeddings.

    Returns:
        dict: A dictionary with averaged embeddings for each lemma.
    """
    average_embeddings = {}
    for lemma, embeddings in lemmas_embeddings.items():
        # Calculate the average embedding for the current lemma
        average_embedding = [sum(vector) / len(vector) for vector in zip(*embeddings)]
        average_embeddings[lemma] = average_embedding
    return average_embeddings