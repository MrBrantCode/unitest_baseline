"""
QUESTION:
Given a list of integers, create a function named `corrected_sequence` that finds the longest progressively ascending subsequence present in the list along with the positions of elements forming that sequence in the original list. The function should return two lists: the longest ascending subsequence and the corresponding indices of its elements in the original list. The function must handle cases where there are multiple subsequences with the same maximum length.
"""

def corrected_sequence(array):
    output_array = []
    output_indices = []
    sequence = [array[0]]
    indices = [0]
    for i in range(1, len(array)):
        if sequence[-1] < array[i]:
            sequence.append(array[i])
            indices.append(i)
        elif sequence[-1] >= array[i]:
            if len(sequence) > len(output_array):
                output_array = sequence[:]
                output_indices = indices[:]
            sequence = [array[i]]
            indices = [i]
    if len(sequence) > len(output_array):
        output_array = sequence
        output_indices = indices
    return output_array, output_indices