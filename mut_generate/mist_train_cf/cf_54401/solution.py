"""
QUESTION:
Write a function `calculate_disparity` that takes two lists, `list1` and `list2`, as input. The function should return a dictionary where the keys are the unique elements present in both lists and the values are the total frequency of these elements in both lists. The function should ignore any elements that are common to both lists. 

Restrictions: 
- The input lists can contain any type of elements (integers, strings, etc.).
- The function should handle duplicate elements within each list.
- The output dictionary should only contain elements that are unique to each list when compared to the other list.
"""

def calculate_disparity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_elements = set1.symmetric_difference(set2)
    frequency_dict = {}

    for element in list1:
        if element in unique_elements:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1

    for element in list2:
        if element in unique_elements:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
    return frequency_dict