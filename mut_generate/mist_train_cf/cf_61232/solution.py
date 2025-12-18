"""
QUESTION:
Design a function named `detect_sequence` that takes a numerical sequence as input and returns "Valid sequence" if the sequence starts with '1' and ends with '9', and "Invalid sequence" otherwise. The function should handle edge cases such as non-sequence inputs, empty sequences, and sequences with less than two elements.
"""

def detect_sequence(sequence):
    # Check if sequence is a list or tuple
    if not isinstance(sequence, (list, tuple)):
        return "Error: Input is not a sequence"
    # Check if sequence is empty
    elif len(sequence) == 0:
        return "Error: Sequence is empty"
    # Check if sequence length is less than 2, because we need at least two different numbers for a valid sequence.
    elif len(sequence) < 2:
        return "Error: Sequence should have at least two numbers"
    # Check if first number is 1 and last number is 9
    elif sequence[0] == 1 and sequence[-1] == 9:
        return "Valid sequence"
    else:
        return "Invalid sequence"