"""
QUESTION:
Design a function `find_sequences` that takes two inputs: a list of distinct large numerical data sets and a list of specific number sequences. The function should return the starting and ending index of each specific number sequence within each data set. The number sequences may overlap with each other, and if an instance of a number sequence is entirely contained in another located sequence, it should be reported as a separate occurrence. The solution should maintain a low time complexity, ideally O(n*m*k), where n is the number of data sets, m is the average length of the data sets, and k is the number of number sequences.
"""

import re

def find_sequences(data, number_sequences):
    """
    Find the starting and ending indices of specific number sequences within each data set.

    Args:
    data (list): A list of distinct large numerical data sets.
    number_sequences (list): A list of specific number sequences.

    Returns:
    A list of dictionaries, where each dictionary contains the sequence, data set index, start index, and end index.
    """

    result = []
    for i, data_set in enumerate(data):
        for sequence in number_sequences:
            for match in re.finditer(sequence, data_set):
                result.append({
                    'sequence': sequence,
                    'data_set_index': i,
                    'start_index': match.start(),
                    'end_index': match.end() - 1
                })
    return result