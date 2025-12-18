"""
QUESTION:
Write a function `find_swap_pairs(sequence)` that takes a list of unique integers as input and returns a dictionary with two keys: 'index' and 'swap_with'. The 'index' key should contain the index of the first element in the sequence that is smaller than its predecessor, and the 'swap_with' key should contain the index of the smallest element to its left that can be swapped with it to potentially sort the sequence in ascending order. If the sequence is already sorted, return {'index': -1, 'swap_with': -1}.
"""

def find_swap_pairs(sequence):
    pair = {'index': -1, 'swap_with': -1}
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i+1]: 
            pair['index'] = i+1
            for j in range(i+1):  
                if sequence[j] < sequence[i+1]:
                    pair['swap_with'] = j
            break
    return pair