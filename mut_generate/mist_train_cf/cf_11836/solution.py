"""
QUESTION:
Implement a function called `find_even_indexes` that takes a list as input and returns the elements at even indexes in reverse order. The function should only include the elements at the 0th, 2nd, 4th, 6th, and so on, indexes from the input list.
"""

def find_even_indexes(lst):
    even_indexes = []
    for i in range(len(lst)):
        if i % 2 == 0:
            even_indexes.append(lst[i])
    return even_indexes[::-1]