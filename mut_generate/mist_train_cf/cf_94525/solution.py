"""
QUESTION:
Write a function `compare_lists(list1, list2)` to compare two lists of objects with 'id' and 'name' attributes. The function should return True if the objects in both lists have the same 'id' and 'name' attributes in the same order, with the condition that an object in list1 with a 'name' attribute that is a substring of an object's 'name' attribute in list2 is considered a match. The function should return False otherwise.
"""

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    for obj1, obj2 in zip(list1, list2):
        if obj1['id'] != obj2['id']:
            return False

        if obj1['name'] not in obj2['name'] and obj2['name'] not in obj1['name']:
            return False

    return True