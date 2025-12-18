"""
QUESTION:
Write a function called `get_permutations` that takes a list of elements as input and returns a list of lists, where each sublist is a unique permutation of the input list.
"""

def get_permutations(input_list): 
    result = [] 
    if len(input_list) == 0: 
        return [] 
    if len(input_list) == 1: 
        return [input_list] 
    for i in range(len(input_list)): 
        x = input_list[i] 
        xs = input_list[:i] + input_list[i+1:] 
        for p in get_permutations(xs): 
            result.append([x] + p) 
    return result