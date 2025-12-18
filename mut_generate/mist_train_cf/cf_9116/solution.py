"""
QUESTION:
Write a function called `group_and_sort` that groups a list of dictionaries by a shared key ('score'), then sorts the groups in descending order based on the sum of the shared key ('score'). If two groups have the same sum, then sort them based on the minimum value of another key ('age').
"""

def group_and_sort(dicts):
    """
    Groups a list of dictionaries by a shared key ('score'), 
    then sorts the groups in descending order based on the sum of the shared key ('score'). 
    If two groups have the same sum, then sort them based on the minimum value of another key ('age').

    Args:
        dicts (list): A list of dictionaries.

    Returns:
        list: A list of lists of dictionaries.
    """

    # Group the list by the shared key 'score'
    grouped_list = {}
    for dictionary in dicts:
        score = dictionary['score']
        if score in grouped_list:
            grouped_list[score].append(dictionary)
        else:
            grouped_list[score] = [dictionary]

    # Sort the groups in descending order based on the sum of the shared key 'score'
    sorted_groups = sorted(grouped_list.values(), key=lambda x: (sum(dictionary['score'] for dictionary in x), -min(dictionary['age'] for dictionary in x)), reverse=True)

    return sorted_groups