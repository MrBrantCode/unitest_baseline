"""
QUESTION:
Implement the `process_sequence_in_batches` function, which takes a list of tuples representing a shuffled sequence of numbers and a batch size as input. The function should process the sequence in batches of the specified size and return a list of lists, where each inner list contains the tuples representing the numbers in each batch. 

The input sequence is a list of tuples, where each tuple contains two integers: the index of the number in the original sequence and the actual number. The batch size is an integer between 1 and the length of the input sequence. The function should return a list of lists, where each inner list contains tuples representing the numbers processed in each batch.
"""

from typing import List, Tuple

def process_sequence_in_batches(sequence_numbers: List[Tuple[int, int]], batch_size: int) -> List[List[Tuple[int, int]]]:
    sequence_numbers.sort(key=lambda x: x[0])  # Sort the input sequence_numbers by the original index
    processed_batches = [sequence_numbers[i:i+batch_size] for i in range(0, len(sequence_numbers), batch_size)]
    return processed_batches