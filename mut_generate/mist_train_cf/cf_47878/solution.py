"""
QUESTION:
Create a recursive function `compare_nested_lists` that takes two arguments, `lst1` and `lst2`, which are lists of lists containing strings. The function should return `True` if both lists contain the same elements, disregarding their sequence and level of nesting, and `False` otherwise. The function should be able to handle lists with different levels of nesting.
"""

def compare_nested_lists(lst1, lst2):
    def flatten(lst): 
        output = []
        for i in lst:
            if isinstance(i, list):
                output.extend(flatten(i))
            else:
                output.append(i)
        return output

    return sorted(flatten(lst1)) == sorted(flatten(lst2))