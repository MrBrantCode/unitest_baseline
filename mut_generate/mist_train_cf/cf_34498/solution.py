"""
QUESTION:
Implement the function `calculate_log_prob` that takes in a sequence of words and a dictionary of vocabulary log probabilities, where each word is associated with a list of floats representing its log probabilities. The function should return the log probability of the sequence according to the log-linear model. If a word is not found in the vocabulary, use the log probabilities for the unknown word. The log-linear model is assumed to have the same number of log probabilities for each word, which is determined by the length of the log probability list for any word in the vocabulary. 

Function Signature: `def calculate_log_prob(words: List[str], vocab_log_probs: Dict[str, List[float]]) -> float:`
"""

from typing import List, Dict

def calculate_log_prob(words: List[str], vocab_log_probs: Dict[str, List[float]]) -> float:
    vocab_size = len(next(iter(vocab_log_probs.values())))
    log_prob = 0.0
    for i, word in enumerate(words):
        if word in vocab_log_probs:
            log_prob += vocab_log_probs[word][i]
        else:
            log_prob += vocab_log_probs['<unk>'][i]
    return log_prob