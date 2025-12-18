"""
QUESTION:
Write a function `delete_elements` that takes two parameters: a list of elements and a list of indices. Delete elements from the list at the specified indices. Handle both positive and negative indices, treating negative indices as counting from the end of the list. If an index is out of range, print an error message and continue deleting elements from the remaining valid indices. The function should have a time complexity of O(n), where n is the length of the list.
"""

def delete_elements(list_of_numbers, indices):
    """
    Deletes elements from the list at the specified indices.
    
    Parameters:
    list_of_numbers (list): A list of numbers
    indices (list): A list of indices
    
    Returns:
    list: The modified list of numbers
    """
    for index in sorted(indices, reverse=True):
        if index >= 0:
            if index < len(list_of_numbers):
                del list_of_numbers[index]
            else:
                print("Error: Index", index, "is out of range")
        else:
            if abs(index) <= len(list_of_numbers):
                del list_of_numbers[index]
            else:
                print("Error: Index", index, "is out of range")
    return list_of_numbers