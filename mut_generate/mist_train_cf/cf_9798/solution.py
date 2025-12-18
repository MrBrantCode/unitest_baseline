"""
QUESTION:
Write a function `combine_and_filter` that takes two lists of dictionaries as input, combines them into one list, filters out dictionaries where the age is less than 21, modifies dictionaries with an age less than 21 to include an additional "status" key-value pair, and returns the sorted list in descending order based on the name attribute.
"""

def combine_and_filter(list1, list2):
    """
    Combines two lists of dictionaries, filters out dictionaries where the age is less than 21, 
    modifies dictionaries with an age less than 21 to include an additional "status" key-value pair, 
    and returns the sorted list in descending order based on the name attribute.

    Args:
        list1 (list): The first list of dictionaries.
        list2 (list): The second list of dictionaries.

    Returns:
        list: The combined, filtered, and sorted list of dictionaries.
    """
    combined_list = list1 + list2
    filtered_list = [d for d in combined_list if d['age'] >= 21 or (d['age'] < 21 and (d.update({'status': 'Underage'}) or True))]
    sorted_list = sorted(filtered_list, key=lambda x: x['name'], reverse=True)
    return sorted_list