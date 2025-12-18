"""
QUESTION:
Design a function named `find_common` that compares two nested sorted lists, `list_one` and `list_two`, and returns a list of common elements. The function should account for duplicate common elements and include them in the resulting list. The input lists may contain non-numeric values and may be nested.
"""

def find_common(list_one, list_two):
    """
    Compares two nested sorted lists and returns a list of common elements.
    The function accounts for duplicate common elements and includes them in the resulting list.

    :param list_one: The first nested sorted list
    :param list_two: The second nested sorted list
    :return: A list of common elements
    """

    def flatten(input_list):
        """
        Flattens a list to remove nested lists
        :param input_list: A nested list
        :return: The flattened list
        """
        flat_list = []
        for i in input_list:
            if isinstance(i, list):  # If element is of type list
                flat_list.extend(flatten(i))  # extends the main list with flattened sublist
            else:
                flat_list.append(i)
        return flat_list

    # Flatten the lists
    flat_list1 = flatten(list_one)
    flat_list2 = flatten(list_two)

    common_list = [value for value in flat_list1 if value in flat_list2]
    return common_list