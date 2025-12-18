"""
QUESTION:
Create a function named `compare_lists` that takes two lists of strings as input and returns a new list containing the elements that are present in both input lists, with the comparison being case-insensitive.
"""

def compare_lists(my_list, pre_defined_list):
    # Convert both lists to lowercase for case-insensitive comparison
    my_list_lower = [element.lower() for element in my_list]
    pre_defined_list_lower = [element.lower() for element in pre_defined_list]

    # Create a new list to store the common elements
    common_elements = []

    # Check each element in my_list
    for element in my_list_lower:
        # If the element is present in pre_defined_list, add it to common_elements
        if element in pre_defined_list_lower:
            common_elements.append(element)

    return common_elements