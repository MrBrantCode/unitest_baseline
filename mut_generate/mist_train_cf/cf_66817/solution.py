"""
QUESTION:
Design a function named 'list_to_set' that transforms a list into a set, ensuring the final output maintains the set data structure. The function should be able to manage nested lists, converting them into nested sets, as well as a combination of lists and other data types within the same set. The function should also handle lists with elements that are lists, dictionaries, tuples, and sets, converting them into their corresponding set equivalents. The function should be able to handle any level of nesting and manage lists of any size, including those with recursive references and circular references.
"""

def list_to_set(data):
    """
    Function to convert a list to a set; managing nested lists and converting them to nested sets.
    """
    # If data is a list convert each item in the list to a set recursively
    if isinstance(data, list):
        return frozenset(list_to_set(item) for item in data)

    # If data is a set convert each item in the set to a set recursively
    elif isinstance(data, set):
        return frozenset(list_to_set(item) for item in data)
  
    # If data is a tuple convert each item in the tuple to a set recursively and convert the tuples into sets.
    elif isinstance(data, tuple):
        return frozenset(list_to_set(item) for item in data)
  
    # If data is a dictionary convert each key value pair to tuple and handle each item in the tuple recursively.
    elif isinstance(data, dict):
        return frozenset(frozenset([list_to_set(k), list_to_set(v)]) for k,v in data.items())

    # If data is not a list, set, tuple or dict just return the data
    else:
        return data