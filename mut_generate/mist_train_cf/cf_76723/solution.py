"""
QUESTION:
Write a function `remove_duplicates(input_list)` that removes duplicate elements from a list while preserving the order of unique elements. The function should achieve this with the minimum time and memory complexity possible. The function should take a list of elements as input and return a list of unique elements.
"""

def remove_duplicates(input_list):
    seen = set()
    output_list = []
    
    for i in input_list:
        if i not in seen:
            output_list.append(i)
            seen.add(i)
    
    return output_list