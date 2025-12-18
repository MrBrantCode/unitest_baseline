"""
QUESTION:
Write a function called `group_list_elements` that takes a list of integers and an integer representing the desired length of sublists as input. The function should return a list of sublists, where each sublist has the specified length and the length of each sublist is a multiple of 3. The original list length must be a multiple of 8. If these conditions are not met, the function should raise an error.
"""

def group_list_elements(lst, sublist_length):
    assert len(lst) % 8 == 0, "Original list length is not a multiple of 8"
    assert sublist_length % 3 == 0, "Sublist length is not a multiple of 3"

    sublists = [lst[i:i+sublist_length] for i in range(0, len(lst), sublist_length)]
    return sublists