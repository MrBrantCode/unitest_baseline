"""
QUESTION:
Categorize the following data structures as scalar, array, hash data organization module, or advanced data structure and provide an argument for the chosen category. The data structures are: Doubly Linked List, Binary Search Tree, Hash Table with Collision handling, Balanced AVL Tree, and Directed Graph with weighted edges.
"""

def categorize_data_structure(data_structure):
    """
    Categorize the given data structure as scalar, array, hash, advanced, or unknown.

    Args:
        data_structure (str): The name of the data structure.

    Returns:
        str: The category of the data structure.
    """

    # Define the categories for each data structure
    categories = {
        "Doubly Linked List": "advanced",
        "Binary Search Tree": "scalar",
        "Hash Table with Collision handling": "hash",
        "Balanced AVL Tree": "scalar",
        "Directed Graph with weighted edges": "advanced"
    }

    # Return the category for the given data structure
    return categories.get(data_structure, "unknown")

# Example usage (Note that this function does not solve the problem but demonstrates the categorization)
print(categorize_data_structure("Doubly Linked List"))  # Output: advanced
print(categorize_data_structure("Binary Search Tree"))  # Output: scalar
print(categorize_data_structure("Hash Table with Collision handling"))  # Output: hash
print(categorize_data_structure("Balanced AVL Tree"))  # Output: scalar
print(categorize_data_structure("Directed Graph with weighted edges"))  # Output: advanced
print(categorize_data_structure("Unknown Data Structure"))  # Output: unknown