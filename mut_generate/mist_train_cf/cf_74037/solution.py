"""
QUESTION:
Create a function named `create_palindromic_sequence` that takes a queue of elements as input and returns a list with the elements arranged in a palindromic sequence. The function should be able to handle any type of elements and any size of queue. The original queue should remain unchanged.
"""

from collections import deque

def create_palindromic_sequence(input_queue):
    """
    This function takes a queue of elements as input and returns a list with the elements arranged in a palindromic sequence.
    
    Args:
        input_queue (deque): A queue of elements.
    
    Returns:
        list: A list of elements in a palindromic sequence.
    """
    sequence_list = list(input_queue)
    sequence_list.extend(reversed(sequence_list))
    return sequence_list