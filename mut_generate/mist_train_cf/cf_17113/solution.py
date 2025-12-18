"""
QUESTION:
Create a function called `create_dict` that takes two lists as input and returns a dictionary. The dictionary should have the unique elements from both lists as keys, and the values should be lists of tuples. Each tuple should contain the index of the element in the first list, the index of the element in the second list, and the total number of occurrences of the element in both lists.
"""

def create_dict(list1, list2):
    dictionary = {}
    for i in range(len(list1)):
        key = list1[i]
        value = (i, -1, list1.count(list1[i]) + list2.count(list1[i]))
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]
            
    for i in range(len(list2)):
        key = list2[i]
        value = (-1, i, list1.count(list2[i]) + list2.count(list2[i]))
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    return dictionary