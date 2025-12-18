"""
QUESTION:
Create a function called `insert_entry` that adds a new key-value pair to a dictionary while preventing duplicate keys. The dictionary is initially created from a list of tuples, where each tuple contains a key-value pair. The function should take the dictionary and the new key-value pair as input, and return the updated dictionary. If the new key already exists in the dictionary, the function should print a message indicating that duplicates are not allowed and return the original dictionary.
"""

def insert_entry(dictionary, entry):
    """
    Inserts a new key-value pair into a dictionary while preventing duplicate keys.

    Args:
        dictionary (dict): The dictionary to insert the entry into.
        entry (tuple): A tuple containing the key-value pair to be inserted.

    Returns:
        dict: The updated dictionary.
    """

    if entry[0] not in dictionary:
        dictionary[entry[0]] = entry[1]
        print(f"New entry {entry} added to the dictionary!")
    else:
        print(f"Entry {entry[0]} already exists in the dictionary. No duplicates allowed.")
    return dictionary