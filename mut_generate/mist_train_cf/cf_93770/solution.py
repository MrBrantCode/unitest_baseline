"""
QUESTION:
Create a function called `flatten_dict` that takes in a dictionary `d` and an optional prefix string, and returns a flattened version of the dictionary. The dictionary can contain any level of nested dictionaries and lists, and the function should be able to handle them. The function should also be used to pre-process a given dataset and convert it into a tabular format using Pandas, and include a way to calculate the average age of each person's friends.
"""

def flatten_dict(d, prefix=''):
    """
    Recursively flatten a dictionary containing nested dictionaries and lists.
    
    Args:
        d (dict): The dictionary to be flattened.
        prefix (str, optional): The prefix to be added to the keys. Defaults to ''.
    
    Returns:
        dict: The flattened dictionary.
    """
    flat_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, prefix + key + '_'))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    flat_dict.update(flatten_dict(item, prefix + key + '_' + str(i) + '_'))
        else:
            flat_dict[prefix + key] = value
    return flat_dict