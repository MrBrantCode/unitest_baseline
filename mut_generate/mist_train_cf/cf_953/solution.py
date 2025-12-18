"""
QUESTION:
Write a function named `combine_lists` that takes two lists of equal length, `list1` and `list2`, as input. The function should return a dictionary where the keys are elements from `list1` and the values are lists of corresponding elements from `list2` that are divisible by 3. If an element in `list1` is repeated, the corresponding value in the dictionary should be a list of all divisible elements from `list2`. The resulting dictionary should be sorted in ascending order based on the keys.
"""

def combine_lists(list1, list2):
    result_dict = {}
    
    # Iterate over the elements of list1 and list2 simultaneously
    for item1, item2 in zip(list1, list2):
        if item2 % 3 == 0:
            if item1 not in result_dict:
                # If the key is not already in the dictionary, add it with a list as the value
                result_dict[item1] = [item2]
            else:
                # If the key is already in the dictionary, append the value to the existing list
                result_dict[item1].append(item2)
    
    # Sort the dictionary based on the keys in ascending order
    sorted_dict = dict(sorted(result_dict.items()))
    
    return sorted_dict