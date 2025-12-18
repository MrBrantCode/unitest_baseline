"""
QUESTION:
Implement a function `dictionary_operations` that demonstrates the average time complexity of common operations in dictionaries, including insertion, deletion, and retrieval. Assume the dictionary will store integer keys and values. The function should take an integer `n` as input, representing the number of key-value pairs to be inserted into the dictionary. The function should return the dictionary after all operations have been performed.

The function should perform the following operations:
- Insert `n` key-value pairs into the dictionary.
- Retrieve and print the value associated with a specific key.
- Delete a key-value pair from the dictionary.

Note that the function does not need to calculate the exact time complexity of these operations, but rather demonstrate how they can be performed in Python.
"""

def dictionary_operations(n):
    """
    Demonstrates the average time complexity of common operations in dictionaries.
    
    Args:
        n (int): The number of key-value pairs to be inserted into the dictionary.
    
    Returns:
        dict: The dictionary after all operations have been performed.
    """
    
    # Initialize an empty dictionary
    dictionary = {}
    
    # Insert n key-value pairs into the dictionary
    for i in range(n):
        dictionary[i] = i * 2
    
    # Retrieve and print the value associated with a specific key
    key = n // 2  # Choose a key in the middle of the range
    print("Value associated with key", key, ":", dictionary[key])
    
    # Delete a key-value pair from the dictionary
    del dictionary[key]
    
    return dictionary