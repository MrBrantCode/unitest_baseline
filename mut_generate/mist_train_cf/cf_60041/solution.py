"""
QUESTION:
Create a function called `concat_verify` that takes two parameters, both of which must be lists. The function should concatenate the two input lists, verify that they are joined correctly, and return the concatenated list if all checks pass. The function should check that the input parameters are indeed lists, the individual elements retain their original order, and the concatenated list has the correct total length. If any of these checks fail, the function should return an error message.
"""

def concat_verify(list1, list2):
    # Check if both inputs are lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        return 'Error: Both inputs must be lists.'
    # Concatenate two lists
    joined_list = list1 + list2
    # Check if lengths of original + joined lists match
    if len(joined_list) != len(list1) + len(list2):
        return 'Error: The lengths of the original and the joined lists do not match.'
    # Check if elements of the original lists are in the joined list in the same order
    for i in range(len(joined_list)):
        if i < len(list1):
            if joined_list[i] != list1[i]:
                return 'Error: The elements of the first list are not in the correct order in the joined list.'
        else:
            if joined_list[i] != list2[i - len(list1)]:
                return 'Error: The elements of the second list are not in the correct order in the joined list.'            
    # All tests passed, return joined list
    return joined_list