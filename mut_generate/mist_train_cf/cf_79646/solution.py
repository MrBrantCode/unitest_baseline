"""
QUESTION:
Write a function `remove_duplicates_nested` that takes a list of numbers as input, which can include nested lists. The function should return a new list where all duplicate numbers are removed, including duplicates within nested lists, without using any built-in Python functions or libraries for removing duplicates.
"""

def remove_duplicates_nested(sequence):
    checked = []
    for i in sequence:
        if type(i) is list:
            i = remove_duplicates_nested(i)
        if i not in checked:
            checked.append(i)
    return checked