"""
QUESTION:
Create a function `convert_list_to_dict` that takes a list of entries in the format [name, age, hobby] and returns a dictionary where each key is the name of the person and the value is a dictionary containing their age (as an integer) and hobby. The resulting dictionary should not contain duplicate entries, should be sorted alphabetically by name, and should have a time complexity of O(n), where n is the number of elements in the list.
"""

def convert_list_to_dict(lst):
    """
    Converts a list of entries in the format [name, age, hobby] into a dictionary 
    where each key is the name of the person and the value is a dictionary containing 
    their age (as an integer) and hobby.

    Args:
        lst (list): A list of entries in the format [name, age, hobby]

    Returns:
        dict: A dictionary where each key is the name of the person and the value is a 
              dictionary containing their age (as an integer) and hobby.
    """
    result = {}
    for i in range(0, len(lst), 3):
        name = lst[i]
        age = int(lst[i+1])
        hobby = lst[i+2]
        result[name] = {'age': age, 'hobby': hobby}
    return dict(sorted(result.items()))