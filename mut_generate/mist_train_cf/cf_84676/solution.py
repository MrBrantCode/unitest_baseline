"""
QUESTION:
Create a function called `dict_of_products` that takes a list of tuples as input, where each tuple contains two integers. The function should return a dictionary where the keys are the first elements of the tuples and the values are lists of products of the first and second elements of the tuples. If a key already exists in the dictionary, the new product should be appended to the existing list.
"""

def dict_of_products(list_of_tuples):
    dict_of_products = {}
    for tup in list_of_tuples:
        if tup[0] not in dict_of_products:
            dict_of_products[tup[0]] = [tup[0]*tup[1]]
        else:
            dict_of_products[tup[0]].append(tup[0]*tup[1])
    return dict_of_products