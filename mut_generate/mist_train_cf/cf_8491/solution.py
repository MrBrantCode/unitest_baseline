"""
QUESTION:
Write a function named `find_duplicates` that takes a list as input and returns a list of tuples, where each tuple contains a duplicate element and its count. The function should be able to handle a list containing both integers and strings, and should not use any built-in functions or data structures other than lists and dictionaries. The time complexity of the function should be O(n), where n is the size of the input list.
"""

def find_duplicates(lst):
    counts = {}

    for element in lst:
        # Handle integers and strings as separate cases
        if isinstance(element, int):
            element_key = str(element) + "_int"
        else:
            element_key = element + "_str"

        if element_key in counts:
            counts[element_key] += 1
        else:
            counts[element_key] = 1

    duplicates = []
    for key, value in counts.items():
        # Extract the element value from the key
        element = key.split("_")[0]
        
        # Extract the data type from the key
        data_type = key.split("_")[1]
        
        # Handle integers and strings as separate cases
        if data_type == "int":
            duplicates.append((int(element), value))
        else:
            duplicates.append((element, value))

    return duplicates