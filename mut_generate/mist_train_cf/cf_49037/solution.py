"""
QUESTION:
Write a function `find_indices` that accepts two lists `list1` and `list2` and a boolean switch. The function should return the indices of elements from `list2` found in `list1`. If the switch is `True`, return all indices of elements from `list2` found in `list1`. If the switch is `False`, return the index of the first occurrence of each element from `list2` found in `list1`. The indices should be returned in the order of the elements in `list2`.
"""

def find_indices(list1, list2, switch):
    # initialize an empty dictionary to store the indices
    indices = {x: [] for x in list2}

    # iterate over the indices and elements in list1
    for i, val in enumerate(list1):
        # if the element is in list2
        if val in indices:
            # add the index to its list in the dictionary
            indices[val].append(i)
    
    # initialize an empty list to store the result
    result = []

    # for each element in list2
    for element in list2:
        # if it was found in list1 (i.e. its list in the dictionary is not empty)
        if indices[element]:
            # if the switch is True, add all indices
            if switch: 
                result.extend(indices[element])
            # if the switch is False, add only the first index
            else: 
                result.append(indices[element][0])
    return result