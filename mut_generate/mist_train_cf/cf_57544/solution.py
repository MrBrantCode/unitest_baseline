"""
QUESTION:
Create a function called `create_nested_dict` that takes a list of nested tuples as input. The input list contains tuples where the first element is another tuple with two elements, and the second element is a value. The function should return a dictionary where the key is the first element of the outer tuple, and the value is another dictionary. The inner dictionary's key is the first element of the inner tuple, and the value is the second element of the inner tuple. The function should handle the possibility of duplicate keys in the outer tuple by merging the inner dictionaries.
"""

def create_nested_dict(list_of_tuples):
    dict_output = {}
    for item in list_of_tuples:
        if item[0][0] in dict_output:
            dict_output[item[0][0]].update({item[0][1]: item[1]})
        else:
            dict_output[item[0][0]] = {item[0][1]: item[1]}
    return dict_output