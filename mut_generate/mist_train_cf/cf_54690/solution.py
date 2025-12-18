"""
QUESTION:
Create a function `count_dict_pairs(data)` that takes a list of dictionaries as input, recursively counts the total number of key-value pairs in each dictionary, including those in nested dictionaries, and returns a list of these counts. The function should handle erroneous input and exceptions, such as non-dictionary items in the list.
"""

def count_dict_pairs(data):
    """
    Counts the total number of key-value pairs in each dictionary in the input list,
    including those in nested dictionaries, and returns a list of these counts.

    Args:
        data (list): A list of dictionaries.

    Returns:
        list: A list of counts of key-value pairs in each dictionary.

    Raises:
        Exception: If an error occurs during execution.
    """

    def count_pairs_in_dict(dictionary):
        """
        Recursively counts the total number of key-value pairs in a dictionary.

        Args:
            dictionary (dict): A dictionary.

        Returns:
            int: The total number of key-value pairs in the dictionary.
        """
        count = 0
        for value in dictionary.values():
            if isinstance(value, dict):
                count += count_pairs_in_dict(value)
            else:
                count += 1
        return count

    count_list = []
    for item in data:
        try:
            if isinstance(item, dict):
                count_list.append(count_pairs_in_dict(item))
            else:
                print(f'Invalid input: {item} is not a dictionary.')
        except Exception as e:
            print(f'Error occurred: {e}')
    return count_list