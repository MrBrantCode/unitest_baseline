"""
QUESTION:
Create a function called `combine_lists_to_dict` that takes two lists of strings as input. Combine these lists into a dictionary where the keys are the strings from the first list and the values are the strings from the second list. The function should ignore strings that contain special characters, remove any whitespace characters from the keys, convert the values to uppercase, and keep only the first occurrence of any duplicate keys. The lengths of the two input lists will always be the same.
"""

def combine_lists_to_dict(list1, list2):
    dictionary = {}
    for i in range(len(list1)):
        key = ''.join(e for e in list1[i] if e.isalnum())
        if key not in dictionary and key != "":
            dictionary[key] = list2[i].upper()
    return dictionary