"""
QUESTION:
Create a function `categorize_names(names)` that groups the given list of names into categories based on the length of the name and sorts each group in reverse alphabetical order. 

The function should take a list of names as input and return a dictionary where the keys are the lengths of the names and the values are lists of names of the corresponding length, sorted in reverse alphabetical order.

Constraints: 
- The input list can contain up to 10^6 names.
- The length of each name will not exceed 100 characters.
- The time complexity should be O(nlogn), where n is the number of names in the list.
- The space complexity should be O(n), where n is the number of names in the list.
"""

def categorize_names(names):
    name_dict = {}

    for name in names:
        length = len(name)
        if length not in name_dict:
            name_dict[length] = []
        name_dict[length].append(name)

    for length in name_dict:
        name_dict[length].sort(reverse=True)

    return name_dict