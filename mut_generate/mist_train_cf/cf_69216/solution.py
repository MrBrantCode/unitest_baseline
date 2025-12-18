"""
QUESTION:
Create a function called `find_position` that takes a list `lst` and an integer `num` as parameters and returns the position of the first occurrence of `num` in `lst`. The function should use recursion and not utilize any built-in functions. If `num` does not exist in `lst`, the function should return "Number not found in list".
"""

def find_position(lst, num, pos=0):
    # If list is empty, the number is not in the list.
    if not lst:
        return "Number not found in list"

    # If the first element in the list matches the specified number, return position.
    if lst[0] == num:
        return pos
    
    # If the list does not match the specified number, call function recursively on the rest of the list.
    else:
        return find_position(lst[1:], num, pos+1)