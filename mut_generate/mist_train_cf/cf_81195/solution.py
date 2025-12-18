"""
QUESTION:
Create a function named `term_detector` that takes two parameters: `sequence` (a list of alphanumeric phrases) and `term` (a unique alphanumeric term). The function should return a tuple containing two values: the recurrence rate of the term within the sequence and a list of indexes where the term is found. The function should also handle the case when the sequence is empty, and its time complexity should be optimal (i.e., O(n), where n is the size of the sequence).
"""

def term_detector(sequence, term):
    """
    Calculate the recurrence rate of a term in a sequence and return its indexes.

    Args:
        sequence (list): A list of alphanumeric phrases.
        term (str): A unique alphanumeric term.

    Returns:
        tuple: A tuple containing the recurrence rate and a list of indexes.
    """
    if not sequence:
        return 0, []
    
    indexes = [i for i, x in enumerate(sequence) if x == term]
    rate = len(indexes) / len(sequence)
    
    return rate, indexes