"""
QUESTION:
Write a function `find_triplets` that takes a sequence `seq` as input. The function should return two values: a list of all unique triplets in the sequence, considering the sequence as circular, and a dictionary where the keys are the triplets and the values are the indices of the first occurrence of each triplet in the sequence. The function should work with any type of elements in the sequence and should handle the case where the input is not a list.
"""

from collections import defaultdict
from itertools import cycle

def find_triplets(seq):
    if not isinstance(seq, list):
        seq = list(seq)
        
    triplet_dict = defaultdict(list)
    list_of_triplets = list()

    sequence = cycle(seq)
    
    triplet = tuple(next(sequence) for _ in range(3))
    index = (0, 1, 2)

    while index[0] < len(seq):
        triplet_dict[triplet].append(index)
        list_of_triplets.append(triplet)
        
        triplet = (triplet[1], triplet[2], next(sequence))
        index = ((index[0]+1)%len(seq), (index[1]+1)%len(seq), (index[2]+1)%len(seq))

        if index[0] == 0:
            break

    for key in triplet_dict:
        if len(triplet_dict[key]) == 1:
            triplet_dict[key] = triplet_dict[key][0]
            
    return list_of_triplets, dict(triplet_dict)