"""
QUESTION:
Create a function named `create_dictionary` that takes a list of tuples as input where each tuple contains a name and an ID. The function should return a dictionary with the ID (converted to an integer) as the key and the full name as the value. If there are duplicate IDs in the list, the function should merge the corresponding full names into a single value for that ID, separated by spaces. The function should not use any built-in Python functions or libraries.
"""

def create_dictionary(my_list):
    dictionary = {}
    
    for name, id in my_list:
        id = int(id)
        if id in dictionary:
            dictionary[id] += ' ' + name
        else:
            dictionary[id] = name
    
    return dictionary