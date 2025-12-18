"""
QUESTION:
Write a function called `data_structure_complexity` with a dictionary as input, where keys are the names of data structures (arrays, linked lists, hash tables, binary search trees, queues, stacks) and values are lists of operations (accessing, searching, inserting, deleting) and their corresponding time complexities in the best, average, and worst-case scenarios. 

Restrictions: 
- The function should return a dictionary with the time complexities for the given data structures and operations.
- The function should not take any other inputs besides the dictionary.
- The time complexities should be represented using Big O notation.
"""

def data_structure_complexity(data_structure_dict):
    """
    Returns a dictionary with time complexities for given data structures and operations.
    
    Args:
        data_structure_dict (dict): A dictionary with data structures as keys and lists of operations as values.
        
    Returns:
        dict: A dictionary with time complexities for the given data structures and operations.
    """

    complexities = {
        "array": {
            "accessing": "O(1)",
            "searching": "O(n)",
            "inserting": "O(1), O(n)",  # Inserting at the end, Inserting at the beginning or in the middle
            "deleting": "O(n)"
        },
        "linked list": {
            "accessing": "O(n)",
            "searching": "O(n)",
            "inserting": "O(1), O(n)",  # Inserting at the beginning or end, Inserting in the middle
            "deleting": "O(n)"
        },
        "hash table": {
            "accessing": "O(1), O(n)",  # Average and best case, Worst case scenario
            "searching": "O(1), O(n)",  # Average and best case, Worst case scenario
            "inserting": "O(1), O(n)",  # Average and best case, Worst case scenario
            "deleting": "O(1), O(n)"   # Average and best case, Worst case scenario
        },
        "binary search tree": {
            "accessing": "O(log n)",
            "searching": "O(log n)",
            "inserting": "O(log n)",
            "deleting": "O(log n)"
        },
        "queue": {
            "accessing": "O(n)",
            "searching": "O(n)",
            "inserting": "O(1)",
            "deleting": "O(1)"
        },
        "stack": {
            "accessing": "O(n)",
            "searching": "O(n)",
            "inserting": "O(1)",
            "deleting": "O(1)"
        }
    }

    result = {}
    for data_structure, operations in data_structure_dict.items():
        result[data_structure] = {}
        for operation in operations:
            if data_structure.lower() in complexities and operation.lower() in complexities[data_structure.lower()]:
                result[data_structure][operation] = complexities[data_structure.lower()][operation.lower()]
            else:
                result[data_structure][operation] = "Unknown"
    
    return result