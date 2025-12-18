"""
QUESTION:
Write a function `generate_pairs(input_list)` that takes a list of elements as input and returns a list of tuples and a dictionary. The list of tuples should contain all possible pairs of consecutive elements from the input list. The dictionary should have the pairs as keys and their indices in the input list as values. If a pair appears multiple times in the input list, the corresponding value in the dictionary should be a list of all its indices.
"""

def generate_pairs(input_list):
    pairs_list = [(input_list[i], input_list[i + 1]) for i in range(len(input_list) - 1)]
    pairs_dict = {}
    for i in range(len(pairs_list)):
        if pairs_list[i] in pairs_dict:
            pairs_dict[pairs_list[i]].append(i)
        else:
            pairs_dict[pairs_list[i]] = [i]
    return pairs_list, pairs_dict