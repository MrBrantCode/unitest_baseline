"""
QUESTION:
Write a recursive function called `multiply_by_two` that takes a list of integers as input, multiplies each integer by 2, and returns the resulting list. The function should also handle non-integer list items by catching the TypeError, printing the index of the non-integer item, and continuing with the rest of the list.
"""

def multiply_by_two(lst, idx=0, new_lst=None):
    if new_lst is None:
        new_lst = []
    if idx == len(lst):
        return new_lst
    else:
        try:
            new_lst.append(lst[idx] * 2)
            return multiply_by_two(lst, idx + 1, new_lst)
        except TypeError:
            print("Non-integer item found at index: ", idx)
            return multiply_by_two(lst, idx + 1, new_lst)