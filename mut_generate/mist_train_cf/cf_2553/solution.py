"""
QUESTION:
Create a function named `create_dictionary` that takes a list of tuples containing names and IDs as input. The function should return a dictionary where the ID (converted to an integer) is the key and the full name is the value. If there are duplicate IDs, merge the full names into a single value for that ID. The function should have a time complexity of O(n), where n is the length of the input list. Do not use any built-in Python functions or libraries.
"""

def create_dictionary(my_list):
    dictionary = {}
    for name, id in my_list:
        id = int(id)
        if id in dictionary:
            dictionary[id] += " " + name
        else:
            dictionary[id] = name
    return dictionary