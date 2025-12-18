"""
QUESTION:
Develop a function named `nested_common` that takes two lists, `list1` and `list2`, as input and returns a list of their common elements. These lists can be arbitrarily nested, and the function should find common elements at any depth while ignoring the nested structure. The function should consider two elements as common if their values are equal, regardless of their original nesting depth in the input lists.
"""

def nested_common(list1, list2):
    def flatten(lis):
        """Function to flatten an arbitrarily nested list."""
        for item in lis:
            if isinstance(item, list):
                for x in flatten(item):
                    yield x
            else: 
                yield item
            
    list1_flat = set(flatten(list1))
    list2_flat = set(flatten(list2))
    
    common = list1_flat.intersection(list2_flat)
    
    return list(common)