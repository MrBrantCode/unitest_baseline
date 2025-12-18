"""
QUESTION:
Write a function called "peculiar_ordering" that takes a list of integers and decimal numbers as input. The function should return the list in an unusual order, following these rules: 
- Start with the smallest value.
- Then, find the maximum among the remaining numbers.
- After that, locate the smallest remaining number not yet in the output, and so forth.
The function must ignore any "None" values in the input list.
"""

def peculiar_ordering(lst):
    # Removing None values
    lst = [i for i in lst if i is not None]
    
    if len(lst) == 0:
        return []

    out_lst = []
    while len(lst) > 0:
        # Adding the smallest element
        min_value = min(lst)
        out_lst.append(min_value)
        lst.remove(min_value)

        # Adding the largest element (if exists)
        if len(lst) > 0:
            max_value = max(lst)
            out_lst.append(max_value)
            lst.remove(max_value)
            
    return out_lst