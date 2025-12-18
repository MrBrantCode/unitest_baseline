"""
QUESTION:
Create a function `find_and_fix_inversions(sequence)` that takes a list of unique integers as input and returns a dictionary. The dictionary should contain the highest index of an element that is not greater or equal to the previous element, the index of the subsequent smaller element that can be swapped with it to potentially correct the sequence, and the corrected sequence after making the swap. If no such element is found, return `{'index': -1, 'swap_value': -1, 'fixed_sequence': sequence}`. The function should only correct the first inversion found in the sequence.
"""

def find_and_fix_inversions(sequence):
    result = {'index': -1, 'swap_value': -1, 'fixed_sequence': sequence}
    max_val = -1  
    max_index = -1
    for index, value in enumerate(sequence):
        if value >= max_val:
            max_val = value
            max_index = index
        else:
            result['index'] = max_index
            result['swap_value'] = max_val
            # make the swap
            sequence[max_index], sequence[index] = sequence[index], sequence[max_index]
            result['fixed_sequence'] = sequence[:]
            break  
    return result