"""
QUESTION:
Create a class with methods "add" and "find" to manage a dictionary. The "add" method should add a key-value pair to the dictionary, where both the key and value are strings with a maximum length of 50 characters. The "find" method should retrieve the value associated with a given key, handling nested dictionaries up to 5 levels deep, where the key is a string with a maximum length of 50 characters and the default value is a string with a maximum length of 50 characters. If the key is not found, the "find" method should return the provided default value.
"""

def entrance(key, value=None, default_value=None):
    """
    Manage a dictionary with add and find operations.

    The "add" operation adds a key-value pair to the dictionary, where both the key and value are strings with a maximum length of 50 characters.

    The "find" operation retrieves the value associated with a given key, handling nested dictionaries up to 5 levels deep, 
    where the key is a string with a maximum length of 50 characters and the default value is a string with a maximum length of 50 characters. 
    If the key is not found, the "find" operation returns the provided default value.

    Args:
        key (str): The key to add or find.
        value (str, optional): The value to add. Defaults to None.
        default_value (str, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        str or None: The value associated with the key, the default value if the key is not found, or None if the operation is add.
    """
    dictionary = entrance.dictionary if hasattr(entrance, 'dictionary') else {}

    def recursive_find(dictionary, key_list, depth):
        if depth == 5:
            return default_value
        if key_list[0] not in dictionary:
            return default_value
        if len(key_list) == 1:
            return dictionary[key_list[0]]
        if isinstance(dictionary[key_list[0]], dict):
            return recursive_find(dictionary[key_list[0]], key_list[1:], depth + 1)
        return default_value

    if value is not None:
        # Add operation
        if not isinstance(key, str) or not isinstance(value, str):
            print("Invalid key or value type. Both should be strings.")
            return
        if len(key) > 50 or len(value) > 50:
            print("Invalid key or value length. Maximum length is 50 characters.")
            return
        dictionary[key] = value
    else:
        # Find operation
        if not isinstance(key, str):
            print("Invalid key type. Key should be a string.")
            return default_value
        if len(key) > 50:
            print("Invalid key length. Maximum length is 50 characters.")
            return default_value

        key_list = key.split('.')
        result = recursive_find(dictionary, key_list, 0)
        entrance.dictionary = dictionary
        return result