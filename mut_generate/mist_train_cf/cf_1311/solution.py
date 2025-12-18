"""
QUESTION:
Create a function `create_dictionary(lst)` that takes a list of integers as input and returns a dictionary. The dictionary should contain key-value pairs where the keys are even integers from the input list, and the values are the sum of all the odd integers that come after the even integer in the list. The dictionary should only include even integers that have odd integers following them.
"""

def create_dictionary(lst):
    dictionary = {}
    i = 0
    while i < len(lst)-1:
        if lst[i] % 2 == 0:
            key = lst[i]
            value = sum([x for x in lst[i+1:] if x % 2 != 0])
            dictionary[key] = value
        i += 1
    return dictionary