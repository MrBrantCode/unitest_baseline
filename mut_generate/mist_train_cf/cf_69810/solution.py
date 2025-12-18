"""
QUESTION:
Write a function `remove_duplicates` that takes a list of dictionaries `lst`, an outer dictionary key `key1`, and an inner dictionary key `key2` as arguments. Remove duplicates from the list of dictionaries based on their values for the given inner key (`key2`) in the inner dictionary (`key1`). The function should return the updated list of dictionaries with duplicates removed.
"""

def remove_duplicates(lst, key1, key2):
    new_list = []
    for item in lst:
        duplicate = False
        for new_item in new_list:
            if new_item[key1][key2] == item[key1][key2]:
                duplicate = True
                break
        if not duplicate:
            new_list.append(item)
    return new_list