"""
QUESTION:
Write a function `change_second_element` that takes a tuple with at least four elements as input and returns a new tuple where the second element is the sum of the first, third, and fourth elements.
"""

def change_second_element(tup):
    my_list = list(tup)
    my_list[1] = my_list[0] + my_list[2] + my_list[3]
    return tuple(my_list)