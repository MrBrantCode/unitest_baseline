"""
QUESTION:
Create a function called `group_list` that takes a list of elements as input and returns a dictionary where each key is an element from the list and its corresponding value is the number of times the element appears in the list.
"""

def group_list(input_list):
    result = {}
    for element in input_list:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result