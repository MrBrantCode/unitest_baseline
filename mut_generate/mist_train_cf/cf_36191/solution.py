"""
QUESTION:
Create a function `create_collection` that manages collections and configurations. The function should take two parameters: `collection_name` and an optional `config_name`. If a collection with the given `collection_name` already exists, return a message indicating that. Otherwise, create a new collection with the given name and, if provided, associate it with the specified `config_name`. Return a message confirming the creation of the collection and, if applicable, the assigned configuration set.
"""

def create_collection(collection_name, config_name=None, collections={}):
    """
    Creates a new collection with the given name and, if provided, associates it with the specified config_name.

    Args:
    - collection_name (str): The name of the collection to be created.
    - config_name (str, optional): The name of the configuration set to be assigned. Defaults to None.

    Returns:
    - str: A message confirming the creation of the collection and, if applicable, the assigned configuration set.
    """
    if collection_name in collections:
        return f"Collection '{collection_name}' already exists"
    else:
        collections[collection_name] = config_name
        if config_name:
            return f"Created collection '{collection_name}' with config-set '{config_name}'"
        else:
            return f"Created collection '{collection_name}'"