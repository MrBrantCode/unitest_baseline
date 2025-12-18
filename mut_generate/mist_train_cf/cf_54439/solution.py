"""
QUESTION:
Write a function `test_equal` that takes a list of lists as input, and for each sublist, checks if all elements are equal. If all elements in a sublist are equal, return the common element; otherwise, return None. If a sublist is empty, also return None. The function should handle exceptions when the sublists contain mixed data types.
"""

def test_equal(lists):
    try:
        result = []
        for sub_list in lists:
            if sub_list:  # checks if the sublist is not empty
                first = sub_list[0]
                if all(elem == first for elem in sub_list):
                    result.append(first)
                else:
                    result.append(None)
            else:
                result.append(None)
        return result
    except TypeError:
        return 'Error: The list elements should be of the same data types.'