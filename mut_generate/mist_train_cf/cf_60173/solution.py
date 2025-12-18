"""
QUESTION:
Design a function `get_pairs(input)` that generates all possible pairs of consecutive elements from a given list or multi-dimensional array. The function should return a list of tuples containing the pairs and a dictionary where the keys represent the pairs and the values correspond to the indices of the pairs in the original list or array. If the same pair appears more than once, the value should be a list of all the indices where the pair is found. The function should be able to handle circular lists or arrays where the last element and the first element can form a pair, and it should be optimized for time complexity to handle large data sets efficiently.
"""

def entrance(input):
    if not input:
        return [], {}

    pairs = []
    pairs_indices = {}

    for i in range(len(input) - 1):
        pair = (input[i], input[i + 1])
        pairs.append(pair)
        
        if pair not in pairs_indices:
            pairs_indices[pair] = [i]
        else:
            pairs_indices[pair].append(i)

    # handle circular lists
    pair = (input[-1], input[0])
    pairs.append(pair)
    
    if pair not in pairs_indices:
        pairs_indices[pair] = [len(input) - 1]
    else:
        pairs_indices[pair].append(len(input) - 1)

    return pairs, pairs_indices