"""
QUESTION:
Write a function named `create_dict` that takes a list of numbers and a boolean as inputs. The function should return a dictionary where each key is a number from the list. If the boolean is True, the value for each key should be the sum of its indices in the list. If the boolean is False, the value for each key should be the number of times that number appears in the list.
"""

def create_dict(lst, bool_val):
    my_dict = {}
    if bool_val:
        for i, n in enumerate(lst):
            if n not in my_dict:
                my_dict[n] = i
            else:
                my_dict[n] += i
    else:
        for n in lst:
            if n not in my_dict:
                my_dict[n] = 1
            else:
                my_dict[n] += 1
    return my_dict