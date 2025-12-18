"""
QUESTION:
Design a function `find_sequence` that takes a numerical data set and a target number sequence as input, and returns the frequency of the sequence and its positions within the data set. The function should efficiently handle large data sets and sequences of varying lengths, and should consider sequences that may be broken across different consecutive numbers. The data set and sequence should be treated as continuous strings of digits.
"""

def find_sequence(dataset, sequence):
    """
    This function finds the frequency of a target number sequence within a numerical data set 
    and returns the frequency and positions of the sequence.

    Args:
        dataset (str): A string of numerical digits.
        sequence (str): A target sequence of numerical digits.

    Returns:
        tuple: A tuple containing the frequency of the sequence and its positions.
    """
    positions = []
    index = 0
    count = dataset.count(sequence)

    # iterate until the sequence is not found anymore
    while index != -1:
        # find() returns -1 if the sequence is not found
        index = dataset.find(sequence, index)
        if index != -1:
            positions.append(index)
            # increment the index to search for next match
            index += 1    

    return count, positions