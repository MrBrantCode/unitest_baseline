"""
QUESTION:
Create a function `combine_lists(list1, list2, common_attribute)` that takes in two lists of dictionaries (`list1` and `list2`) and a string representing the common attribute between the elements of both lists. Combine the lists into a dictionary where the keys are the values of the `common_attribute` and the values are the merged dictionaries of matching elements.
"""

def combine_lists(list1, list2, common_attribute):
    combined_dict = {}
    for element1 in list1:
        for element2 in list2:
            if element1[common_attribute] == element2[common_attribute]:
                combined_dict[element1[common_attribute]] = {**element1, **element2}
                break
    return combined_dict