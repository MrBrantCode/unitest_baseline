"""
QUESTION:
Write a function `difficult_find_swap_pairs(sequence)` that takes a sequence of unique numbers as input. Iterate over the sequence from the end to the beginning to find the highest index `i` where the value at index `i` is less than its predecessor. If such an index is found, then find the index `j` of the next lower item that can be swapped with the value at index `i` to potentially correct the sequence. Return a dictionary with keys 'index' and 'swap_with' representing the indices `i` and `j` respectively. If no such index `i` is found, return {'index': -1, 'swap_with': -1}.
"""

def difficult_find_swap_pairs(sequence):
    index = -1
    swap_with = -1
    for i in range(len(sequence) - 1, 0, -1):
        if sequence[i] < sequence[i - 1]:
            index = i
            for j in range(i - 1, -1, -1):
                if sequence[j] < sequence[i]:
                    swap_with = j
                    break
            break
    return {'index': index, 'swap_with': swap_with}