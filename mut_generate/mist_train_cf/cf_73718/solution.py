"""
QUESTION:
Create a function `remove_duplicate_elements` that takes a list of numbers as input and returns a new list with duplicate elements removed, preserving the original order. The function should not use sets or built-in functions. The list may contain duplicate numbers, and the order of elements is significant.
"""

def remove_duplicate_elements(input_list):
    hash_map = {} 
    output_list = [] 

    for element in input_list: 
        if element not in hash_map: 
            output_list.append(element) 
            hash_map[element] = True 

    return output_list 