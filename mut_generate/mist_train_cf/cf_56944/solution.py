"""
QUESTION:
Create a function `check_identical(list1, list2)` that verifies whether two lists containing string elements, potentially nested, are identical. The lists are considered identical if they contain the same elements with the same frequency, disregarding sequence and case. The function should handle nested lists and return a boolean value indicating whether the lists are identical or not.
"""

def check_identical(list1, list2):
    """Check if two lists are identical"""
    def flatten(items):
        """Flatten a nested list"""
        flat_list = []
        for i in items:
            if isinstance(i, list):
                flat_list.extend(flatten(i))
            else:
                flat_list.append(i.lower()) 
        return flat_list

    # Flatten the lists
    flat_list1 = flatten(list1)
    flat_list2 = flatten(list2)

    # Sort the lists
    flat_list1.sort()
    flat_list2.sort()
    
    return flat_list1 == flat_list2 # Return whether or not the lists are identical