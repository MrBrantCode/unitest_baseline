"""
QUESTION:
Create a function `group_and_sort` that takes a list of dictionaries and two key names as input. The function should group the dictionaries by the first key and sort the groups in descending order based on the sum of the values of the first key. If two groups have the same sum, they should be sorted based on the minimum value of the second key. The function should return a list of the sorted groups.
"""

def group_and_sort(lst, key1, key2):
    """
    This function groups a list of dictionaries by the first key and sorts the groups in descending order based on the sum of the values of the first key.
    If two groups have the same sum, they are sorted based on the minimum value of the second key.

    Args:
        lst (list): A list of dictionaries.
        key1 (str): The first key to group and sort by.
        key2 (str): The second key to sort by in case of a tie.

    Returns:
        list: A list of the sorted groups.
    """
    # Group the list by the shared key
    grouped_list = {}
    for dictionary in lst:
        value = dictionary[key1]
        if value in grouped_list:
            grouped_list[value].append(dictionary)
        else:
            grouped_list[value] = [dictionary]

    # Sort the groups in descending order based on the sum of the shared key
    sorted_groups = sorted(grouped_list.values(), key=lambda x: sum(dictionary[key1] for dictionary in x), reverse=True)

    # Sort the groups with the same sum based on the minimum value of the other key
    sorted_groups = sorted(sorted_groups, key=lambda x: min(dictionary[key2] for dictionary in x))

    return sorted_groups