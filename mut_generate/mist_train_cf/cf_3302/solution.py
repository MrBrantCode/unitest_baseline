"""
QUESTION:
Implement a function called "print_names" that takes a list of dictionaries as input and returns a list of name values. The function should iterate over each dictionary in the list, retrieve the value of the "name" key, and handle the following cases: if the "name" key is missing, return "Unknown"; if the "name" key exists but its value is an empty string, return "Empty"; otherwise, return the actual name value. The function should have a time complexity of O(n), where n is the number of dictionaries in the input list.
"""

def print_names(data):
    names = []
    for obj in data:
        name = obj.get("name")
        if name is None:
            names.append("Unknown")
        elif name == "":
            names.append("Empty")
        else:
            names.append(name)
    return names