"""
QUESTION:
Create a function called `compare_lists` that compares two multi-level nested lists containing strings. The function should return True if the lists contain the same elements and sub-elements regardless of their sequence at any level, and False otherwise. The lists can be arbitrary in their depth and do not need to be symmetrical.
"""

def compare_lists(list1, list2):
    """ Compare nested lists disregarding the order """

    def flatten_list(nested_list):
        """ Transform a multi level nested list into a flat list """
        flat_list = []
        for x in nested_list:
            if(isinstance(x, list)):
                flat_list.extend(flatten_list(x))
            else:
                flat_list.append(x)
        return flat_list

    flat_list1 = sorted(flatten_list(list1))
    flat_list2 = sorted(flatten_list(list2))

    return flat_list1 == flat_list2