"""
QUESTION:
Write a function called `categorize_names` that takes a list of names as input and returns a dictionary where the keys are the lengths of the names and the values are lists of names of corresponding lengths, sorted in reverse alphabetical order. The function should have a time complexity of O(nlogn) and space complexity of O(n), where n is the number of names in the list.
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