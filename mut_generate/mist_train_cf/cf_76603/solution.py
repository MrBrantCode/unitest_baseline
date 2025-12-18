"""
QUESTION:
Write a function called `remove_uneven` to remove uneven elements from a nested mixed tuple. The function should be able to handle tuples within tuples and remove uneven elements from them as well. It should also handle a mix of integers, floats, and strings. If a string is numeric and even, it should be kept. If it's not numeric or not even, it should be removed. The function should return a tuple containing only the even numeric elements of the original tuple.
"""

def remove_uneven(lst):
    new_lst = []
    for i in lst:
        if type(i) == tuple:
            new_lst.append(remove_uneven(i))
        elif type(i) == str:
            if i.isdigit() and int(i) % 2 == 0:
                new_lst.append(int(i))
        elif type(i) in (int, float) and i % 2 == 0:
            new_lst.append(i)
    return tuple(new_lst)