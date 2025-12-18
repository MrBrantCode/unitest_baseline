"""
QUESTION:
Create a function named `common_elements` that takes three lists `l1`, `l2`, `l3` as input. The function should return a list of common elements that appear in all three lists under the same index. The function should handle lists of different lengths by returning common elements up to the length of the shortest list. It should also support elements of any data type, including integers, strings, and floating point numbers, as well as nested lists, returning common elements in the same nested structure.
"""

def entance(l1, l2, l3):
    common = []
    for i, value in enumerate(l1):
        try:
            if l1[i] == l2[i] == l3[i]:
                common.append(l1[i])
        except IndexError:
            break      
        except TypeError:  # Nested list
            # Recursive call to handle nested lists
            if (isinstance(value, list) and
                i < len(l2) and
                i < len(l3) and
                isinstance(l2[i], list) and
                isinstance(l3[i], list)):
                common.append(entance(l1[i], l2[i], l3[i]))
    return common