"""
QUESTION:
Write a function `remove_carrots` that takes a list of strings as input, removes all occurrences of the string "Carrots" except the first one, and returns the modified list. If the input list is empty, return an empty list.
"""

def remove_carrots(lst):
    if not lst:
        return []
    new_lst = []
    carrot_encountered = False
    for item in lst:
        if item != "Carrots" or not carrot_encountered:
            new_lst.append(item)
            if item == "Carrots":
                carrot_encountered = True
    return new_lst