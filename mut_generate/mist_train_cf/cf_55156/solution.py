"""
QUESTION:
Create a function `permute_list` that generates all possible permutations of a given integer list without using any built-in methods for permutations. The function should take a list as input and return a list of lists, where each sublist is a permutation of the input list. The function should be implemented recursively and should handle lists of any length, including empty lists and lists with a single element.
"""

def permute_list(lst):
    if len(lst) == 0:
        return []

    elif len(lst) == 1:
        return [lst]

    else:
        lst_permutations = []

        for i in range(len(lst)):
            current_item = lst[i] 
            remaining_list = lst[:i] + lst[i+1:]
            
            for p in permute_list(remaining_list):
                lst_permutations.append([current_item] + p)
        return lst_permutations