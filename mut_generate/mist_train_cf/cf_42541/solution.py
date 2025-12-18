"""
QUESTION:
Implement a function `process_sequences` that takes a list of sequences and a configuration dictionary as input, and returns a modified list of sequences. The function should truncate each sequence to a specified maximum length and terminate it at the index of the first occurrence of a specific value if present.

The function must take two parameters: 
- `sequences`: A list of sequences, where each sequence is a list of integers.
- `config`: A dictionary containing two keys: `'early_stop'` representing the value at which the sequence should be terminated, and `'max_seq_len'` representing the maximum length to which the sequence should be truncated.

The function should return a list of modified sequences based on the specified criteria.
"""

from typing import List, Dict

def process_sequences(sequences: List[List[int]], config: Dict[str, int]) -> List[List[int]]:
    early_stop = config['early_stop']
    max_seq_len = config['max_seq_len']
    processed_sequences = []
    
    for seq in sequences:
        if early_stop in seq:
            idx = seq.index(early_stop)
            processed_seq = seq[:idx]
        else:
            processed_seq = seq[:max_seq_len]
        processed_sequences.append(processed_seq)
    
    return processed_sequences