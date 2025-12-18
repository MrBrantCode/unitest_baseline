"""
QUESTION:
Create a function `handle_new_vocabulary` that generates embeddings for new, unseen hashtags without requiring the retraining of the original embedding model. The function should be able to handle out-of-vocabulary words and produce a vector representation for them. Assume that the original model cannot be updated, and the function should work with the existing model.
"""

def handle_new_vocabulary(model, new_hashtag):
    """
    Generate an embedding for a new, unseen hashtag without retraining the original model.
    
    Args:
    model (object): The original embedding model.
    new_hashtag (str): The new, unseen hashtag.
    
    Returns:
    list: A vector representation of the new hashtag.
    """
    
    # Split the hashtag into sub-words (n-grams)
    sub_words = [new_hashtag[i: j] for i in range(len(new_hashtag)) for j in range(i + 1, len(new_hashtag) + 1)]
    
    # Initialize the vector representation with zeros
    vector_representation = [0.0] * model.vector_size
    
    # For each sub-word, add its vector representation to the overall vector representation
    for sub_word in sub_words:
        if sub_word in model:
            vector_representation = [a + b for a, b in zip(vector_representation, model[sub_word])]
    
    # Average the vector representation
    vector_representation = [x / len(sub_words) for x in vector_representation]
    
    return vector_representation