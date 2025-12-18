"""
QUESTION:
Develop a function 'detectDupesWithIndex' that identifies duplicate elements in a given tuple and returns a dictionary with the duplicates and their first and last index positions. If there are no duplicates, return an empty dictionary. The function should take a tuple as input and return a dictionary where each key is a duplicate element and its corresponding value is another dictionary with 'first_index' and 'last_index' as keys.
"""

def detectDupesWithIndex(input_tuple):
    result = {}
    for i, element in enumerate(input_tuple):
        if input_tuple.count(element) > 1:
            if element not in result:
                result[element] = {'first_index': input_tuple.index(element), 'last_index': len(input_tuple) - 1 - input_tuple[::-1].index(element)}
    return result