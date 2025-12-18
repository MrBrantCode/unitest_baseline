"""
QUESTION:
Create a function named `convert_dict_to_tuples` that takes a dictionary as input and returns a list of tuples. The dictionary may contain nested dictionaries as values. The output list should contain tuples where each tuple represents a key-value pair from the dictionary, with nested dictionaries flattened and represented as single key-value pairs in the tuples, using a dot notation to combine keys (e.g., "friends.Alice.address.city"). The output list should be sorted based on the keys in ascending order.
"""

def convert_dict_to_tuples(dictionary):
    """
    This function takes a dictionary as input, including nested dictionaries, 
    and returns a list of tuples representing key-value pairs. 
    Nested dictionaries are flattened and represented as single key-value pairs 
    using a dot notation to combine keys.

    Args:
    dictionary (dict): The input dictionary.

    Returns:
    list: A list of tuples, where each tuple contains a key-value pair.
    """

    def flatten_dict(nested_dict, prefix=""):
        """
        Helper function to recursively flatten the dictionary.

        Args:
        nested_dict (dict): The dictionary to be flattened.
        prefix (str): The prefix to be added to the key.

        Yields:
        tuple: A tuple containing the key-value pair.
        """
        for key, value in sorted(nested_dict.items()):
            new_key = f"{prefix}{key}" if prefix else key
            if isinstance(value, dict):
                yield from flatten_dict(value, new_key + ".")
            else:
                yield (new_key, value)

    return list(flatten_dict(dictionary))