"""
QUESTION:
Create a function `process_list_elements` that takes a list `elements` as input. The function should handle lists with non-uniform data types, complex data structures (e.g., dictionaries, lists of dictionaries), nested data structures (e.g., lists containing lists or dictionaries), and non-hashable elements. The function should be optimized for performance and memory usage, especially for extremely large lists. The function should return a dictionary where each key is a unique element from the list and its corresponding value is a list of indices where the element appears in the original list.
"""

def process_list_elements(elements):
    element_dict = {}

    def add_element_to_dict(element, index):
        if element not in element_dict:
            element_dict[element] = [index]
        else:
            element_dict[element].append(index)

    def process_element(element, index):
        if isinstance(element, (str, int, float)):
            add_element_to_dict(element, index)
        elif isinstance(element, list):
            for sub_element in element:
                process_element(sub_element, index)
        elif isinstance(element, dict):
            for sub_element in element.values():
                process_element(sub_element, index)

    for i, element in enumerate(elements):
        process_element(element, i)

    return element_dict