"""
QUESTION:
Write a function `permute` to generate all unique permutations of a given list of elements, where the list can contain repeated elements, strings, and numbers. The function should consider strings and numbers with the same value as distinct elements, and it should handle input lists of up to 10 elements. The function should output the permutations as lists, preserving the original type of each element.
"""

def permute(data, i=0): 
    """
    Generate all unique permutations of a given list of elements.
    
    Args:
        data (list): The input list containing elements of any type.
        i (int, optional): The index to start the permutation. Defaults to 0.
    
    Returns:
        list: A list of permutations where each permutation is a list of elements.
    """
    if i == len(data): 
        return [data[:]]  # Return a copy of the current permutation
    permutations = []
    seen = set()
    for j in range(i, len(data)): 
        str_data_j = str(data[j])
        if str_data_j not in seen:
            seen.add(str_data_j)
            data[i], data[j] = data[j], data[i] 
            permutations.extend(permute(data, i + 1)) 
            data[i], data[j] = data[j], data[i] 
    return permutations