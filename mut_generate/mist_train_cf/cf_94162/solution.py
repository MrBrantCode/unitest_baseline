"""
QUESTION:
Write a function called `sort_and_filter_people` that takes two lists of dictionaries, `list1` and `list2`, as input. Each dictionary represents a person with keys 'name', 'age', and 'gender'. The function should combine these two lists into one, filter out any dictionaries where the age is less than 21, and modify those dictionaries to include an additional key-value pair where the key is "status" and the value is "Underage". The function should return the combined list sorted first by gender in ascending order (Male before Female) and then by name in descending order, with case-insensitive sorting.
"""

def sort_and_filter_people(list1, list2):
    """
    Combines two lists of dictionaries representing people, filters out those under 21, 
    adds a 'status' key to those under 21, and sorts the list by gender and name.

    Args:
        list1 (list): First list of dictionaries.
        list2 (list): Second list of dictionaries.

    Returns:
        list: Combined and sorted list of dictionaries.
    """
    combined_list = list1.copy()
    combined_list.extend(list2)

    # Since we need to add 'status' to those under 21, we filter after adding 'status'
    for d in combined_list:
        if d['age'] < 21:
            d['status'] = 'Underage'

    filtered_list = [d for d in combined_list if d['age'] >= 21 or 'status' in d]

    sorted_list = sorted(filtered_list, key=lambda x: (x['gender'].lower(), x['name'].lower()[::-1]))

    return sorted_list