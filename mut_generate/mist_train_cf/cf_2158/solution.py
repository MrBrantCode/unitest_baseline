"""
QUESTION:
Create a function named `convert_list_to_dict` that takes a list as input and returns a dictionary. The dictionary should contain unique items from the list as keys and their first occurrence position in the list as values. The dictionary should be sorted in descending order based on the values, and if two values are equal, they should be sorted alphabetically in ascending order.
"""

def convert_list_to_dict(lst):
    dict = {}
    for i in range(len(lst)):
        if lst[i] not in dict:
            dict[lst[i]] = i
    sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1], item[0]))}
    return sorted_dict