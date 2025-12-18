"""
QUESTION:
Create a function named `unique_tuple` that accepts a list of mixed data types, including nested lists. The function should flatten all nested lists, remove duplicates while preserving order (in Python 3.7 and above), and return a tuple of unique elements. The function should not contain any additional external parameters besides the input list.
"""

def unique_tuple(input_list):
    def flatten_list_nested(l):
        result = []
        for i in l:
            if isinstance(i, list):
                result += flatten_list_nested(i)
            else:
                result.append(i)
        return result

    flattened_list = flatten_list_nested(input_list)
    unique_elements = list(dict.fromkeys(flattened_list)) # Using dict.fromkeys() to preserve order in Python 3.7+
    return tuple(unique_elements)