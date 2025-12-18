"""
QUESTION:
Write a function `convert_to_tuple` that takes a list of dictionaries as input and returns a tuple of namedtuples. The input list contains dictionaries with the keys "name", "age", "gender", and "city". The function should use the `namedtuple` function from the `collections` module to define a new datatype for the tuple entries. The output should be a tuple where each element is an instance of the defined namedtuple.
"""

from collections import namedtuple

def convert_to_tuple(lst):
    # define the new datatype using namedtuple
    Person = namedtuple('Person', 'name age gender city')
    
    # use a list comprehension to convert each dictionary to the namedtuple
    return tuple(Person(**d) for d in lst)