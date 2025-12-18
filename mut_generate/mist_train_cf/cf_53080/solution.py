"""
QUESTION:
Develop a function named find_swap_pairs that identifies the maximum index of an element that breaks the increasing sequence and the subsequent smaller element's index with which it can be swapped to possibly rectify the sequence. If no such element exists, return {'index': -1, 'swap_with': -1}. Assume the input sequence has distinct elements.
"""

def find_swap_pairs(sequence):
    # we iterate the sequence from the end to start
    for i in range(len(sequence) - 1, 0, -1):
        # if we've found the element that breaks the increasing sequence
        if sequence[i] < sequence[i - 1]:
            # we iterate from the end to start to find the swap candidate
            for j in range(len(sequence) - 1, i - 1, -1):
                # if we've found the element smaller than the breaking element
                if sequence[j] < sequence[i - 1]:
                    # we return the information about these two elements
                    return {'index': i - 1, 'swap_with': j}
    # if there's no pair to be swapped
    return {'index': -1, 'swap_with': -1}