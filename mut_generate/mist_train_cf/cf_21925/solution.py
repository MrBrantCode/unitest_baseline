"""
QUESTION:
Write a function named `filter_and_sort_names` that takes a list of names as input and returns a new list containing only the names that start with the letter "J" and have more than 5 characters. The returned list should be sorted in alphabetical order. The function should have a time complexity of O(nlogn), where n is the length of the input list, and should not use any built-in sorting or filtering functions, external libraries or modules, or additional data structures apart from the input list and necessary loop counters or indices.
"""

def filter_and_sort_names(data):
    """
    Filters a list of names to include only those that start with 'J' and have more than 5 characters, 
    then sorts the result in alphabetical order.

    Args:
        data (list): A list of names

    Returns:
        list: A list of filtered and sorted names
    """
    filtered_names = []
    for name in data:
        if len(name) > 5 and name[0] == 'J':
            filtered_names.append(name)
    
    # Sorting the filtered names in alphabetical order
    for i in range(len(filtered_names)):
        for j in range(i+1, len(filtered_names)):
            if filtered_names[i] > filtered_names[j]:
                filtered_names[i], filtered_names[j] = filtered_names[j], filtered_names[i]
    
    return filtered_names