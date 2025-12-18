"""
QUESTION:
Write a function named `filter_string` that filters an array of strings and nested sub-arrays to return only the entries containing a given symbol sequence of up to 3 characters. The function should take two parameters: the input array and the symbol sequence. The input array can contain a mix of strings and sub-arrays of strings. The function should return a list of strings that include the given symbol sequence.
"""

def filter_string(list_elements, sequence):
    filtered = []

    for i in list_elements: 
        if isinstance(i, list): 
            for j in i: 
                if sequence in j: filtered.append(j)
        else: 
            if sequence in i: filtered.append(i)
            
    return filtered