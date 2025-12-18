"""
QUESTION:
Create a function named `substitute_alphanumeric` that takes two lists of alphanumeric strings as input, `in_list` and `out_list`, and substitutes every occurrence of the strings in `in_list` with their corresponding strings from `out_list` at the same index. The function should return the modified list. Note that `in_list` and `out_list` must have the same length, and any string in `in_list` without a corresponding substitution in `out_list` should remain unchanged.
"""

def substitute_alphanumeric(in_list, out_list):
    # Create a dictionary with mapped values
    substitute_dict = {in_list[i]: out_list[i] for i in range(len(in_list))}
    
    # Make the substitution
    res = [substitute_dict[i] if i in substitute_dict else i for i in in_list]
    
    return res