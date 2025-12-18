"""
QUESTION:
Develop a function named `pair_data` that takes a list of varying lengths and data types as input. The function should return a list of tuples containing all possible pairs of sequential elements derived from the input list and a dictionary where the keys are the pairs and the values are the indices of the pairs in the original list. If the same pair appears more than once, the value should be a list of all the indices where the pair appears.
"""

def pair_data(input_list):
    pair_list = [(input_list[i], input_list[i+1]) for i in range(len(input_list)-1)]
    pair_dict = {}
    for i, pair in enumerate(pair_list):
        if pair in pair_dict:
            pair_dict[pair].append(i)
        else:
            pair_dict[pair] = [i]
    return pair_list, pair_dict