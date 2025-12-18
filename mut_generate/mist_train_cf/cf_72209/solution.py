"""
QUESTION:
Create a function named `get_non_repeating_elements` that takes a list of elements and returns a list of elements that appear only once in the original list, in the order of their appearance. Design a custom data structure in a separate helper function named `manage_elements` to organize the elements and store the count of each element. The data structure should not use built-in Python data structures such as dictionaries or sets. The function should return the non-repeating elements when called with a list of elements.
"""

class UniqElements:
    def __init__(self):
        self.elements = []
        self.seen = {}

    def add_element(self, el):
        if el not in self.seen:
            self.seen[el] = 1
            self.elements.append(el)
        else:
            self.seen[el] += 1

    def get_unique_elements(self):
        return [el for el in self.elements if self.seen[el] == 1]

def manage_elements(s: list):
    uniq_elem = UniqElements()
    for el in s:
        uniq_elem.add_element(el)
    return uniq_elem.get_unique_elements()

def get_non_repeating_elements(s: list):
    return manage_elements(s)