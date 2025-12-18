"""
QUESTION:
Implement a function `preprocess_sequences` that truncates and pads a list of sequences to a specified maximum length, initializes an embeddings layer with a given matrix, sets an initial learning rate, and adds sinusoidal frequencies to the embeddings if specified.

The function should take the following parameters: 
- `sequences`: A list of lists, where each inner list represents a sequence of integers.
- `max_seq_length`: An integer representing the maximum length to which longer sequences should be truncated.
- `padding_value`: An integer representing the value with which shorter sequences should be padded.
- `learning_rate`: A float representing the initial learning rate.
- `emb_matrix`: A NumPy array representing an embeddings matrix.
- `trainable_embeddings`: A boolean indicating whether the embeddings matrix should be trainable.
- `embedding_dim`: An integer representing the dimensionality of token (word) embeddings.
- `is_positional`: A boolean indicating whether sinusoids of different frequencies should be added to the embeddings.

The function should return a NumPy array representing the preprocessed sequences and a float representing the initial learning rate.
"""

import numpy as np
from typing import List, Tuple

def preprocess_sequences(sequences: List[List[int]], 
                         max_seq_length: int, 
                         padding_value: int, 
                         learning_rate: float, 
                         emb_matrix: np.ndarray, 
                         trainable_embeddings: bool, 
                         embedding_dim: int, 
                         is_positional: bool) -> Tuple[np.ndarray, float]:
    preprocessed_sequences = [seq[:max_seq_length] + [padding_value] * (max_seq_length - len(seq)) if len(seq) < max_seq_length else seq[:max_seq_length] for seq in sequences]
    
    initial_learning_rate = learning_rate
    
    if is_positional:
        sinusoids = np.array([np.sin(pos / 10000 ** (2 * i / embedding_dim)) if i % 2 == 0 else np.cos(pos / 10000 ** (2 * i / embedding_dim)) for pos in range(max_seq_length) for i in range(embedding_dim)])
        emb_matrix = np.concatenate((emb_matrix, sinusoids.reshape((max_seq_length, embedding_dim))), axis=1)
    
    return np.array(preprocessed_sequences), initial_learning_rate