"""
QUESTION:
For an artificial corpus with documents composed of multiple non-natural language sentences, design a tokenization approach and language model training strategy for downstream tasks like sentence classification or clustering with sentence BERT. Consider the following restrictions:

- Tokenization: Determine the optimal tokenization approach, either by sentence (`<s>sentence1</s><s>sentence2</s>`) or by document (`<s>the whole document</s>`).
- Training: Decide which type of model to train, either Masked Language Model (MLM), Next Sentence Prediction (NSP), or both, depending on the importance of sentence relationships and order within the documents.
"""

def entance(corpus, downstream_task):
    """
    This function determines the optimal tokenization approach and language model training strategy 
    for downstream tasks like sentence classification or clustering with sentence BERT.

    Args:
    corpus (list): A list of documents, where each document is a list of sentences.
    downstream_task (str): The specific task the model is intended for, e.g., 'sentence classification', 'clustering'.

    Returns:
    tuple: A tuple containing the optimal tokenization approach and the type of model to train.
    """
    
    # Tokenization approach
    tokenization_approach = 'sentence'
    
    # Model training strategy
    if downstream_task in ['sentence classification', 'clustering']:
        model_training_strategy = 'MLM'
    else:
        model_training_strategy = 'MLM and NSP'
    
    return tokenization_approach, model_training_strategy