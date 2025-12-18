"""
QUESTION:
Write a function named `create_dict` that takes a list of tuples as input where each tuple contains a shape name and a number. The function should return a dictionary where the shape names are keys and the numbers are values. If the input list contains duplicate shape names with different numbers, the function should keep the first key-value pair and ignore any following pairs with the same key.
"""

def create_dict(shapes_list):
    shape_dictionary = dict()
    for i in shapes_list:
        if i[0] not in shape_dictionary:
            shape_dictionary[i[0]] = i[1]
    return shape_dictionary