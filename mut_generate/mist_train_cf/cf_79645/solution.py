"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of elements as input, loops through the list with their corresponding indexes, removes duplicates, and handles exceptions during execution. The function should print the index and value of each element and return a list of unique elements.
"""

def remove_duplicates(input_list):
    """
    This function removes duplicates from a list, prints index and value of each element, 
    and handles exceptions during execution.

    Args:
        input_list (list): The list to remove duplicates from.

    Returns:
        list: A list of unique elements.
    """
    try:
        unique_list = []
        for index, element in enumerate(input_list):
            print(f"Index: {index}, Element: {element}")
            
            if element not in unique_list:
                unique_list.append(element)

        return unique_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return None