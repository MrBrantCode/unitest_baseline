"""
QUESTION:
Create a function `construct_hash_table` that constructs a hash table from a given list where each node's data serves as the key and its node's position in the list serves as the value. Handle collisions with separate chaining. The input is a list of integers and the output is a dictionary where the keys are the integers from the list and the values are lists of their corresponding positions.
"""

def construct_hash_table(input_list):
    """
    Construct a hash table from a given list where each node's data serves as the key 
    and its node's position in the list serves as the value. Handle collisions with 
    separate chaining.

    Args:
        input_list (list): A list of integers.

    Returns:
        dict: A dictionary where the keys are the integers from the list and the 
        values are lists of their corresponding positions.
    """

    hash_table = {}
    
    for index, value in enumerate(input_list):
        if value in hash_table:
            hash_table[value].append(index)
        else:
            hash_table[value] = [index]
        
    return hash_table